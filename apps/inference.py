
import requests
import os
import sys
import cv2
import json
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__),'../../../'))

from components.Rotation.src.models.PackageModel import PackageConfigs,ConfigExecutor,PackageModel,RotationExecutor,RotationInputs,RotationConfigs,RotationRequest,InputImage,Degree,KeepSideBBox,KeepSideTrue,KeepSideFalse
from sdks.novavision.src.base.model import Image, Request
from sdks.novavision.src.media.image import Image as image


ENDPOINT_URL = "http://127.0.0.1:8000/api"

def infer():
    imread = cv2.imread("/opt/project/components/Rotation/resources/yorkshire_terrier.jpg")
    image_obj = Image(
        name="DemoImage",
        uID="001",
        mimeType="image/jpg",
        encoding="bytes",
        value=imread,
        type="Image"
    )
    image_obj = image.encode64(image_obj)
    inputImage = InputImage(value=image_obj)
    degree = Degree(value=45)
    keepsideBBoxFalse = KeepSideFalse(value=False)
    keepsideBBoxTrue = KeepSideTrue(value=True)
    drawBBox = KeepSideBBox(value=keepsideBBoxTrue)
    rotationInputs = RotationInputs(inputImage=inputImage)
    rotationConfigs = RotationConfigs(degree=degree, drawBBox=drawBBox)
    rotationRequest = RotationRequest(inputs=rotationInputs, configs=rotationConfigs)
    rotationExecutor = RotationExecutor(value=rotationRequest)
    executor = ConfigExecutor(value=rotationExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    request = PackageModel(configs=packageConfigs, name="Rotation")
    request_json = json.loads(request.json())
    response = requests.post(ENDPOINT_URL, json = request_json)
    print(response.raise_for_status())
    print(response.json())


if __name__ =="__main__":
    infer()