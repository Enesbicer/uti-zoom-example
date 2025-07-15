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

    def TextWriter(self,img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1.2
        thickness = 2
        color = (255, 255, 255)

        (text_width, text_height), _ = cv2.getTextSize(self.textWriterText, font, font_scale, thickness)
        h, w = img.shape[:2]

        if self.configTypeTextWriter== "Center":
            x = (w - text_width) // 2
            y = (h + text_height) // 2
        elif self.configTypeTextWriter== "Top":
            x = (w - text_width) // 2
            y = text_height + 10
        else:
            x, y = 10, 30  # fallback default


        cv2.putText(self.image, self.textWriterText, (x + 2, y + 2), font, font_scale, (0, 0, 0), thickness + 1, cv2.LINE_AA)

        cv2.putText(self.secondImage, self.textWriterText, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
        return img


    def run(self):
        img1 =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img2 = Image.get_frame(img=self.secondImage, redis_db=self.redis_db)
        img1.value=self.TextWriter(img1.value, img2.value)
        self.image = Image.set_frame(img=img1, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_texwriter(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
