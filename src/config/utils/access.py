from abc import ABCMeta, abstractmethod
from jsonschema import validate
import json
import os 
from .schema import schemas
from lib.dict import dotdict

CONFIG_PATH = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/..')
del os

class _Config(metaclass=ABCMeta):
  @property
  @abstractmethod
  def schema(self):
    pass
  @property
  @abstractmethod
  def id(self):
    pass

  def __init__(self):
    with open(f'{CONFIG_PATH}/{self.location}') as jsonFile:
      jsonData = json.load(jsonFile)
      self.validate(jsonData)
      self.data = dotdict(jsonData)
  def validate(self, json):
    validate(json, self.schema)
  def update(self, jsonData):
    self.validate(jsonData)
    self.data = dotdict(jsonData)
  def get(self):
    return self.data


class _Screen(_Config):
  id = 'screen'
  location = 'screen.json'
  schema = schemas['screen']
  def __init__(self):
    super().__init__()

class _Theme(_Config):
  id = 'theme'
  location = 'theme.json'
  schema = schemas['theme']
  def __init__(self):
    super().__init__()

class _AnimatorInstances(_Config):
  id = 'animator-instances'
  location = 'animator-instances.json'
  schema = schemas['animator-instances']
  def __init__(self):
    super().__init__()
  def validate(self, jsonData):
    super().validate(jsonData)
    # TODO check that the columns equal 12
    # TODO check that serial keys exist in serialUnits

class _SerialUnits(_Config):
  id = 'serial-units'
  location = 'serial-units.json'
  schema = schemas['serial-units']
  def __init__(self):
    super().__init__()



# essentially singleton classes
screen = _Screen()
theme = _Theme()
serialUnits = _SerialUnits()
animatorInstances = _AnimatorInstances()
