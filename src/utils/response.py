
from sdks.novavision.src.helper.package import PackageHelper
from components.ZoomExample.src.models.PackageModel import (PackageModel, PackageConfigs,
ConfigExecutor, ZoomExampleExecutor,ZoomExampleExecutorResponse,ZoomExampleExecutorOutputs,OutputImage,TextWriterExecutorOutputs,TextWriterExecutorResponse,TextWriterExecutor,OutputSecondImage)


def build_response_zoom(context):
    outputImage = OutputImage(value=context.image)
    zoomExampleExecutorOutputs = ZoomExampleExecutorOutputs(outputImage=outputImage)
    zoomExampleExecutorResponse=ZoomExampleExecutorResponse(outputs=zoomExampleExecutorOutputs)
    zoomExampleExecutor=ZoomExampleExecutor(value=zoomExampleExecutorResponse)
    configExecutor=ConfigExecutor(value= zoomExampleExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_textwriter(context):
    outputImage = OutputImage(value=context.image)
    outputSecondImage = OutputSecondImage(value=context.image)
    textWriterExecutorOutputs = TextWriterExecutorOutputs(outputImage=outputImage, outputSecondImage=outputSecondImage)
    textWriterExecutorResponse = TextWriterExecutorResponse(outputs=textWriterExecutorOutputs)
    textWriterExecutor = TextWriterExecutor(value=textWriterExecutorResponse)
    configExecutor = ConfigExecutor(value=textWriterExecutor)
    packageConfigs = PackageConfigs(executor=configExecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
