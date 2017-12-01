import pyglet
from pyglet import gl
from abc import ABCMeta, abstractmethod
from config.utils.access import screen

class animator(metaclass=ABCMeta):
  # an identifier that is used by the animator-instances.json file
  @property
  @abstractmethod
  def id(self):
    pass
  # used to check if the given array of serial keys is the correct amount
  @property
  @abstractmethod
  def numSerialKeys(self):
    pass
  # the number of columns (out of 12) that the given animator will occupy
  @property
  @abstractmethod
  def columnsTaken(self):
    pass

  def __init__(self, serialKeys, column, theme, color_override={}):
    # sets up helper values used in most classes
    self.column = column
    self.serialKeys = serialKeys
    # sets the color for the animator using theme as a base and overriding color names if they exist
    self.color_pallete = dict(theme['color_pallete'], **color_override)
    screen_instance = screen.get()
    self.width_of_animator = screen_instance.width * ( self.columnsTaken / screen_instance.num_columns )
    self.origin = (
      screen_instance.width / screen_instance.num_columns * self.column,
      0
    )
    self.central_origin = (
      self.origin[0] + self.width_of_animator / 2,
      screen_instance.height / 2
    )

    # does some safety checks on the values
    if (self.numSerialKeys > 0 and len(self.serialKeys) != self.numSerialKeys):
      raise ValueError(f'{self.id} requires exactly {self.numSerialKeys} serial key(s), not {len(self.serialKeys)}')

  @abstractmethod
  def update(self, reducedSerialDict):
    pass
  @abstractmethod
  def select(self, serialDict):
    pass
  @abstractmethod
  def draw(self):
    pass
  def delete(self):
    for sprite in self.sprites.values():
      sprite.delete()
