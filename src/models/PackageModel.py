from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class InputSecondImage(Input):
    name: Literal["inputSecondImage"] = "inputSecondImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputSecondImage(Output):
    name: Literal["outputSecondImage"] = "outputSecondImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class TextWriterText(Config):
    """
         Resimde görünmesini istediğiniz yazıyı girininiz
    """
    name: Literal["textWriterText"] = "textWriterText"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Text Writer Input"

class Left(Config):
    configEdit: TextWriterText
    name:Literal["Left"] = "Left"
    value:Literal["Left"] = "Left"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Left"

class Right(Config):
    configEdit: TextWriterText
    name:Literal["Right"] = "Right"
    value:Literal["Right"] = "Right"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Right"

class Bottom(Config):
    configEdit: TextWriterText
    name:Literal["Bottom"] = "Bottom"
    value:Literal["Bottom"] = "Bottom"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Bottom"

class Top(Config):
    configEdit: TextWriterText
    name:Literal["Top"] = "Top"
    value:Literal["Top"] = "Top"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Top"
class Center(Config):
    configEdit: TextWriterText
    name:Literal["Center"] = "Center"
    value:Literal["Center"] = "Center"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Center"
class ConfigTypeTextWriter(Config):
    """
        Yazınızın resimde ki konumu.
    """
    name: Literal["configTypeTextWriter"] = "configTypeTextWriter"
    value: Union[Center,Top,Left,Right,Bottom]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Text Writer"








class BorderColorGreen(Config):
    name: Literal["ColorBlack"] = "ColorBlack"
    value: Literal["Black"] = "Black"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Green"


class BorderColorBlue(Config):
    name: Literal["ColorBlack"] = "ColorBlack"
    value: Literal["Black"] = "Black"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Blue"

class BorderColorRed(Config):
    name: Literal["ColorBlack"] = "ColorBlack"
    value: Literal["Black"] = "Black"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Red"

class BorderColorBlack(Config):
    name: Literal["ColorBlack"] = "ColorBlack"
    value: Literal["Black"] = "Black"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Black"





class BorderColor(Config):
    """
        Apply the border
    """
    name: Literal["BorderColor"] = "BorderColor"
    value: Union[]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Border Color"





class BorderSolid(Config):
    configEdit: BorderColor
    name: Literal["BorderSolid"] = "BorderSolid"
    value: Literal["BorderSolid"] = "BorderSolid"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Solid"



class BorderDouble(Config):
    configEdit: BorderColor
    name: Literal["BorderDouble"] = "BorderDouble"
    value: Literal["BorderDouble"] = "BorderDouble"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Double"


class BorderDashed(Config):
    configEdit: BorderColor
    name: Literal["BorderDashed"] = "BorderDashed"
    value: Literal["BorderDashed"] = "BorderDashed"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Dashed"



class BorderStyle(Config):
    """
        Apply the border
    """
    name: Literal["BorderStyle"] = "BorderStyle"
    value: Union[BorderDashed,BorderSolid,BorderDouble]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Border Style"











class BorderFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class BorderTrue(Config):
    configEdit:BorderStyle
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class BorderApplier(Config):
    """
        Apply the border
    """
    name: Literal["BorderApplier"] = "BorderApplier"
    value: Union[BorderTrue, BorderFalse]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Border Applier"




















class ZoomVariable(Config):
    """
         Ne kadar zoom yapmak istediğinizi yüzdelik üzerinden giriniz.
    """
    name: Literal["zoomVariable"] = "zoomVariable"
    value: int = Field(default=1, ge=1, le=100)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["integers between [0, 100]"] = "integers between [0, 100]"

    class Config:
        title = "Zoom Percentage"

class TextWriterExecutorInputs(Inputs):
    inputImage: InputImage
    inputSecondImage: InputSecondImage


class TextWriterExecutorConfigs(Configs):
    configTypeTextWriter : ConfigTypeTextWriter


class TextWriterExecutorOutputs(Outputs):
    outputImage: OutputImage
    outputSecondImage: OutputSecondImage

class TextWriterExecutorRequest(Request):
    inputs: Optional[TextWriterExecutorInputs]
    configs: TextWriterExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }

class TextWriterExecutorResponse(Response):
    outputs: TextWriterExecutorOutputs

class TextWriterExecutor(Config):
    name: Literal["TextWriterExecutor"] = "TextWriterExecutor"
    value: Union[TextWriterExecutorRequest, TextWriterExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "TextWriterExecutor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class ZoomExampleExecutorInputs(Inputs):
    inputImage: InputImage


class ZoomExampleExecutorConfigs(Configs):
    zoomVariable:ZoomVariable


class ZoomExampleExecutorOutputs(Outputs):
    outputImage: OutputImage

class ZoomExampleExecutorRequest(Request):
    inputs: Optional[ZoomExampleExecutorInputs]
    configs: ZoomExampleExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }

class ZoomExampleExecutorResponse(Response):
    outputs: ZoomExampleExecutorOutputs

class ZoomExampleExecutor(Config):
    name: Literal["ZoomExampleExecutor"] = "ZoomExampleExecutor"
    value: Union[ZoomExampleExecutorRequest, ZoomExampleExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "ZoomExampleExecutor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[ZoomExampleExecutor,TextWriterExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["ZoomExample"] = "ZoomExample"





