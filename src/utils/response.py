
from sdks.novavision.src.helper.package import PackageHelper
from components.Rotation.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, RotationOutputs, RotationResponse, RotationExecutor, OutputImage


def build_response(context):
    outputImage = OutputImage(value=context.image)
    Outputs = RotationOutputs(outputImage=outputImage)
    rotationResponse = RotationResponse(outputs=Outputs)
    rotationExecutor = RotationExecutor(value=rotationResponse)
    executor = ConfigExecutor(value=rotationExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel