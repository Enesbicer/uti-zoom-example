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
        self.zoomVariable=self.request.param("zoomVariable")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def zoom(self,img):
        self.reHeight = int(img.shape[0] * (100 + self.zoomVariable) / 100)
        self.reWidth = int(img.shape[1] * (100 + self.zoomVariable) / 100)
        down_points = (self.reWidth, self.reHeight)
        resized_image = cv2.resize(img, down_points, interpolation=cv2.INTER_LINEAR)
        return resized_image

    def run(self):
        img =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img.value=self.zoom(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_zoom(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()