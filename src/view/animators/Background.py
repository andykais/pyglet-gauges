import pyglet
from .. import AbstractAnimator

class animator(AbstractAnimator.animator):
  id = 'background'
  numSerialKeys = 0
  columnsTaken = 12

  def __init__(self, groups, batch, theme, column, serialKeys, color_override={}):
    super().__init__(serialKeys, column, theme, color_override)

    self.background_image = pyglet.image.load(theme.images.background)
    self.sprites = {
      'background': pyglet.sprite.Sprite(self.background_image, batch=batch, group=groups['background']),
    }

  def update(self, _):
    pass
  def select(self, _):
    pass
