import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.ZoomExample.src.utils.response import build_response_texwriter
from components.ZoomExample.src.models.PackageModel import PackageModel

class TextWriterExecutor(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.textWriterText = self.request.get_param("textWriterText")
        self.imageFirst = self.request.get_param("inputFirstImage")
        self.imageSecond = self.request.get_param("inputSecondImage")
        self.configTypeTextWriter = self.request.get_param("configTypeTextWriter")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def TextWriter(self,img):
        return  img[50:180, 100:300]


    def run(self):
        img =Image.get_frame(img=self.image,redis_db=self.redis_db)
        img.value=self.TextWriter(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_texwriter(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()