import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.ZoomExample.src.utils.response import build_response_textwriter
from components.ZoomExample.src.models.PackageModel import PackageModel

class TextWriterExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.textWriterText = self.request.get_param("textWriterText")
        self.image = self.request.get_param("inputImage")
        self.secondImage = self.request.get_param("inputSecondImage")
        self.configTypeTextWriter = self.request.get_param("configTypeTextWriter")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def TextWriter(self,img1,img2):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2.0
        thickness = 3
        color = (255, 255, 255)  # Beyaz text
        shadow_color = (0, 0, 0)  # Siyah gölge

        (text_width, text_height), _ = cv2.getTextSize(self.textWriterText, font, font_scale, thickness)
        h, w = img1.shape[:2]


        if self.configTypeTextWriter == "Center":
            x = (w - text_width) // 2
            y = (h + text_height) // 2
        elif self.configTypeTextWriter == "Top":
            x = (w - text_width) // 2
            y = text_height + 20
        else:
            x, y = 50, 50


        if x < 0: x = 10
        if y < text_height: y = text_height + 10
        if x + text_width > w: x = w - text_width - 10
        if y > h - 10: y = h - 20



        cv2.putText(img1, self.textWriterText, (x + 3, y + 3), font, font_scale, shadow_color, thickness + 1,
                    cv2.LINE_AA)
        cv2.putText(img1, self.textWriterText, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)


        cv2.putText(img2, self.textWriterText, (x + 3, y + 3), font, font_scale, shadow_color, thickness + 1,
                    cv2.LINE_AA)
        cv2.putText(img2, self.textWriterText, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

        return img1, img2

    def run(self):
        img1 =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img2 = Image.get_frame(img=self.secondImage, redis_db=self.redis_db)
        img1.value, img2.value = self.TextWriter(img1.value, img2.value)
        self.image = Image.set_frame(img=img1, package_uID=self.uID, redis_db=self.redis_db)
        self.secondImage = Image.set_frame(img=img2, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_textwriter(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
