import pyglet
from . import AbstractAnimator
from serial import getSerialInfo
from lib import calculations, text

class animator(AbstractAnimator.animator):
  def __init__(self, batch, groups, serialKeys=[], column=0, color=(255,255,255), needleColor=(0,0,0)):
    if (len(serialKeys) != 1):
      raise ValueError('serial keys needs to be exactly 1 len long')
    self.serialKey= serialKeys[0]

    #  textImage = text.textArc('0 2 4 6 8 10 12 14 16')
    #  print(textImage.width)
    #  self.textSprite = pyglet.sprite.Sprite(textImage, x=0, y=0, batch=batch, group=groups['text'])

    gauge_image = pyglet.image.load('./assets/gauge.png')
    image_columns = 3
    needle_image = pyglet.image.load('./assets/needlepng.png')
    needle_image.anchor_x = needle_image.width // 2 + 50
    needle_image.anchor_y = needle_image.height // 2
    self.sprite = pyglet.sprite.Sprite(gauge_image,
        batch=batch,
        group=groups['gauges'],
        x=gauge_image.width * column / image_columns,
        y=0)
    self.needleSprite = pyglet.sprite.Sprite(needle_image,
        x=gauge_image.width // 2 + gauge_image.width * column / image_columns,
        y=10,
        batch=batch,
        group=groups['needles'])
    self.sprite.color = color
    self.needleSprite.color = needleColor
    self.needleSprite.rotation = 0
  def update(self, dataPoint):
    attributeInfo = getSerialInfo()[self.serialKey]
    targetRotation = calculations.percentageBetween(attributeInfo.min, attributeInfo.max, dataPoint)
    self.needleSprite.update(
        rotation=self.needleSprite.rotation + (180 * targetRotation - self.needleSprite.rotation) / 30
        )
  def select(self, serialData):
    return serialData[self.serialKey]
  def draw(self):
    pass
