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
from components.Rotation.src.utils.response import build_response
from components.Rotation.src.models.PackageModel import PackageModel


class Rotation(Component):
    def __init__(self, request, bootstrap):
        """
           Constructs of all necessary parameters for rotation process.
           Parameters
           ----------
           images : image list
               image to be rotated
           height: integer
               image height value
           width : integer
               image width value
           rotation_degree : integer
               rotation angle value
        """
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def rotation(self, image):
        """
            height and width of image are extracted from image
            center of image is calculated with (height / 2, width / 2)
            rotation matrix is found using center of image and rotation degree
            image rotates with cv2.warpAffine()
            return rotated image
        """
        if self.keep_side == True:
            height, width = image.shape[:2]
            image_center = (width / 2, height / 2)
            rotation_arr = cv2.getRotationMatrix2D(image_center, self.rotation_degree, 1)
            abs_cos = abs(rotation_arr[0, 0])
            abs_sin = abs(rotation_arr[0, 1])
            bound_w = int(height * abs_sin + width * abs_cos)
            bound_h = int(height * abs_cos + width * abs_sin)
            rotation_arr[0, 2] += bound_w / 2 - image_center[0]
            rotation_arr[1, 2] += bound_h / 2 - image_center[1]
            img_rotation = cv2.warpAffine(image, rotation_arr, (bound_w, bound_h))

            return img_rotation

        elif self.keep_side == False:
            height, width = image.shape[:2]
            rotation_arr = cv2.getRotationMatrix2D((height / 2, width / 2), self.rotation_degree, 1)
            img_rotation = cv2.warpAffine(image, rotation_arr, (height, width))

            return img_rotation

    def run(self):
        """
           Rotate the picture clockwise or counterclockwise depending on the angle.

            Example:
                >> rotation angle value = 30
                >> rotated 30 degrees clockwise
                >> rotation angle value = -30
                >> rotated 30 degrees counterclockwise
        """
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.rotation(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()