
from sdks.novavision.src.helper.package import PackageHelper
from components.ZoomExample.src.models.PackageModel import (PackageModel, PackageConfigs,
ConfigExecutor, ZoomExampleExecutor,ZoomExampleExecutorResponse,ZoomExampleExecutorOutputs,OutputImage)


def build_response(context):
    outputImage = OutputImage(value=context.image)
    zoomExampleExecutorOutputs = ZoomExampleExecutorOutputs(outputImage=outputImage)
    zoomExampleExecutorResponse=ZoomExampleExecutorResponse(outputs=zoomExampleExecutorOutputs)
    zoomExampleExecutor=ZoomExampleExecutor(value=zoomExampleExecutorResponse)
    configExecutor=ConfigExecutor(value= zoomExampleExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel