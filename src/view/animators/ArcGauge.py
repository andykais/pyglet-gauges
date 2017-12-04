import pyglet
# local imports
from .. import AbstractAnimator
from ..primitives import Arc
from lib import calculations
from config.utils.access import serialUnits, screen

class animator(AbstractAnimator.animator):
  id = 'arc-gauge'
  numSerialKeys = 1
  columnsTaken = 4

  def __init__(self, batch, groups, theme, serialKeys=[], column=0, color_override={}):
    super().__init__(serialKeys, column, theme, color_override)

    self.sprites = {
      'gauge': Arc.animator(self.central_origin, 70, color=self.color_pallete['primary'], batch=batch, group=groups['gauges']),
      'border': Arc.animator(self.central_origin, 73, alphaRadius=68, color=self.color_pallete['dull'], batch=batch, group=groups['gauges']),
      'needle': Arc.animator(
        self.central_origin,
        65,
        alphaRadius=20,
        percentage=0.5,
        color=self.color_pallete['accent'],
        batch=batch,
        group=groups['needles'])
    }
    #  TODO investigate order affecting shared verticies

  def update(self, dataPoint):
    attributeInfo = serialUnits.get()[self.serialKeys[0]]
    targetPercentage = calculations.percentageBetween(attributeInfo['min'], attributeInfo['max'], dataPoint)
    self.sprites['needle'].update(targetPercentage)
  def select(self, serialData):
    return serialData[self.serialKeys[0]]
