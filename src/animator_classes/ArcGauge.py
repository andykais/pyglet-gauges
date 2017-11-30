import pyglet
from pyglet import gl
# local imports
from . import AbstractAnimator
from .primitives import Arc
from serial import getSerialInfo
from lib import calculations

class animator(AbstractAnimator.animator):
  def __init__(self, batch, groups, serialKeys=[], column=0, color=(255,255,255), needleColor=(0,0,0)):
    if (len(serialKeys) != 1):
      raise ValueError('serial keys needs to be exactly 1 len long')
    self.serialKey = serialKeys[0]
    needleRadius = 170.6
    taken_columns = 3
    origin = (1024 / taken_columns * column - (1024 / taken_columns) / 2, 150 / 2)
    self.gauge = Arc.animator(origin, 75, color=color, batch=batch, group=groups['gauges'])
    self.border = Arc.animator(origin, 75, alphaRadius=70, color=(0,0,0), batch=batch, group=groups['gauges'])
    #  TODO investigate order affecting shared verticies
    self.needle = Arc.animator(
        origin,
        65,
        alphaRadius=20,
        percentage=0.5,
        color=needleColor,
        batch=batch,
        group=groups['needles'])
  def update(self, percentage):
    self.needle.update(percentage)
    pass
  def select(self, serialData):
    return serialData[self.serialKey]
    pass
  def draw(self):
    pass
