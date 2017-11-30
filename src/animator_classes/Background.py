import pyglet
from . import AbstractAnimator

class animator(AbstractAnimator.animator):
  def __init__(self, groups, batch):
    self.background_image = pyglet.image.load('./assets/background.png')
    self.sprite = pyglet.sprite.Sprite(self.background_image, batch=batch, group=groups['background']),
  def update(self, _):
    pass
  def select(self, _):
    pass
  def draw(self):
    pass
