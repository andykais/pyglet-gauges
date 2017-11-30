import pyglet
from pyglet import gl
from abc import ABC, abstractmethod

class animator(ABC):
  def __init__(self):
    self.name = "abstract animator"
  @abstractmethod
  def update(self, reducedSerialDict):
    pass
  @abstractmethod
  def select(self, serialDict):
    pass
  @abstractmethod
  def draw(self):
    pass
