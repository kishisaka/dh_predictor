from dataclasses import dataclass
from attributes import Attributes
from jsonconstants import JSONConstants


@dataclass
class Person:
    name: str
    attributes: Attributes

    def __init__(self, json):
        self.name = json[JSONConstants.name]
        self.attributes = Attributes(json[JSONConstants.attributes])
