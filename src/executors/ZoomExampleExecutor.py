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
        self.borderApplier = self.request.get_param("borderApplier")
        self.borderColor = self.request.get_param("borderColor")
        self.borderStyle = self.request.get_param("borderStyle")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def zoom(self, image):
        h, w = image.shape[:2]
        zoom_factor = 1 + (self.zoomVariable / 100)
        new_h = int(h / zoom_factor)
        new_w = int(w / zoom_factor)
        center_y = h // 2
        center_x = w // 2
        start_y = center_y - new_h // 2
        start_x = center_x - new_w // 2
        cropped = image[start_y:start_y + new_h, start_x:start_x + new_w]
        zoomed = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)

        # Eğer Border Applier false ise, doğrudan dön
        if not self.borderApplier:
            return zoomed

        # BorderColor seçimi
        color_map = {
            "Black": (0, 0, 0),
            "Blue": (255, 0, 0),
            "Red": (0, 0, 255),
            "Green": (0, 255, 0),
        }
        color = color_map.get(self.borderColor.capitalize(), (0, 0, 0))

        thickness = 4

        if self.borderStyle == "borderSolid":
            cv2.rectangle(zoomed, (0, 0), (w - 1, h - 1), color, thickness)

        elif self.borderStyle == "borderDashed":
            step = 20
            for i in range(0, w, step * 2):
                cv2.line(zoomed, (i, 0), (min(i + step, w - 1), 0), color, thickness)
                cv2.line(zoomed, (i, h - 1), (min(i + step, w - 1), h - 1), color, thickness)
            for i in range(0, h, step * 2):
                cv2.line(zoomed, (0, i), (0, min(i + step, h - 1)), color, thickness)
                cv2.line(zoomed, (w - 1, i), (w - 1, min(i + step, h - 1)), color, thickness)

        elif self.borderStyle == "borderDouble":
            offset = 6
            cv2.rectangle(zoomed, (0, 0), (w - 1, h - 1), color, thickness)
            cv2.rectangle(zoomed, (offset, offset), (w - 1 - offset, h - 1 - offset), color, thickness)

        return zoomed


    def run(self):
        img =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img.value=self.zoom(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_zoom(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
