import pyglet
from .. import AbstractAnimator
from config.utils.access import serialUnits
from lib import calculations, text

class animator(AbstractAnimator.animator):
  id = 'half-circle-wide-needle'
  numSerialKeys = 1
  columnsTaken = 4

  def __init__(self, batch, groups, theme, serialKeys=[], column=0, color_override={}):
    super().__init__(serialKeys, column, theme, color_override)

    #  textImage = text.textArc('0 2 4 6 8 10 12 14 16')
    #  print(textImage.width)
    #  self.textSprite = pyglet.sprite.Sprite(textImage, x=0, y=0, batch=batch, group=groups['text'])

    gauge_image = pyglet.image.load(theme.images.half_circle)
    needle_image = pyglet.image.load(theme.images.wide_needle)
    needle_image.anchor_x = needle_image.width // 2 + 50
    needle_image.anchor_y = needle_image.height // 2
    self.sprites = {
      'gauge': pyglet.sprite.Sprite(gauge_image,
        batch=batch,
        group=groups['gauges'],
        x=self.origin[0],
        y=0),
      'needle': pyglet.sprite.Sprite(needle_image,
        x=self.central_origin[0],
        y=10,
        batch=batch,
        group=groups['needles'])
    }
    self.sprites['gauge'].color = self.color_pallete['primary']
    self.sprites['needle'].color = self.color_pallete['accent']
    self.sprites['needle'].rotation = 0

  def update(self, dataPoint):
    attributeInfo = serialUnits.get()[self.serialKeys[0]]
    targetRotation = calculations.percentageBetween(attributeInfo['min'], attributeInfo['max'], dataPoint)
    needleSprite = self.sprites['needle']
    needleSprite.update(
        rotation=needleSprite.rotation + (180 * targetRotation - needleSprite.rotation) / 30
        )
  def select(self, serialData):
    return serialData[self.serialKeys[0]]
