"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.ZoomExample.src.utils.response import build_response_zoom
from components.ZoomExample.src.models.PackageModel import PackageModel


class ZoomExampleExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.zoomVariable=self.request.get_param("zoomVariable")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def zoom(self,image):
        h, w = image.shape[:2]
        scale = self.zoomVariable / 100.0

        # Yeni kırpılacak boyut
        new_h = int(h * scale)
        new_w = int(w * scale)

        # Orta noktayı bul
        center_y = h // 2
        center_x = w // 2

        # Kırpılacak bölgenin başlangıç koordinatları
        start_y = center_y - new_h // 2
        start_x = center_x - new_w // 2

        # Kırp ve yeniden boyutlandır
        cropped = image[start_y:start_y + new_h, start_x:start_x + new_w]
        zoomed = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)

        return zoomed


    def run(self):
        img =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img.value=self.zoom(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_zoom(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()