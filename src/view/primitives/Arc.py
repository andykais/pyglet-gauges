import pyglet
from pyglet import gl
from math import pi, cos, sin, fabs
# local imports
from .. import AbstractAnimator
from lib import calculations


# fast technique taken from [SiegeLord's Abode](http://slabode.exofire.net/circle_draw.shtml)
def getArcCoords(origin, radius, alpha_radius=0, clockwise=True, start_angle=(pi * 1.5)):
  smoothness = 100
  verts = []
  theta = ( 2 * pi ) / smoothness
  c = cos(theta)
  s = sin(theta)
  t1, t2 = -1, -1
  x1 = radius * cos(start_angle)
  y1 = radius * sin(start_angle)
  x2 = alpha_radius * cos(start_angle)
  y2 = alpha_radius * sin(start_angle)
  for i in range(smoothness + 1):
    t1 = x1
    t2 = x2
    x1 = c * x1 - s * y1
    y1 = s * t1 + c * y1
    x2 = c * x2 - s * y2
    y2 = s * t2 + c * y2
    verts += [
        x1 + origin[0],
        y1 + origin[1],
        x2 + origin[0],
        y2 + origin[1],
        ]
  # reverse each pair of points
  if (clockwise):
    for i in range(0, len(verts) // 2, 4):
      verts[i    ], verts[-i - 4] = verts[-i - 4], verts[i    ] # reverse x1
      verts[i + 1], verts[-i - 3] = verts[-i - 3], verts[i + 1] # reverse y1
      verts[i + 2], verts[-i - 2] = verts[-i - 2], verts[i + 2] # reverse y2
      verts[i + 3], verts[-i - 1] = verts[-i - 1], verts[i + 3] # reverse x2
  return verts


class animator(AbstractAnimator.animator):
  id = 'primitive-arc'
  numSerialKeys = 0
  columnsTaken = 3

  def __init__(self, origin, radius, batch, group, percentage=1, alphaRadius=0, color=(255,255,255)):
    self.origin = origin
    self.radius = radius
    self.percentage = percentage
    self.alphaRadius = 0
    self.color = color
    self.verticies = getArcCoords(origin, radius, alphaRadius)
    pointsDrawn = len(self.verticies) // 2
    self.colorPoints = color * pointsDrawn
    self.sprites = {}
    self.vertex_list = batch.add(pointsDrawn, gl.GL_QUAD_STRIP, group,
      ('v2f/static', self.verticies),
      ('c3B/static', self.colorPoints))
    #  self.sprites = {
      #  'vertex_list': 
    #  }
    self.__slice_points()
  def __slice_points(self):
    coordsRemaining = int(len(self.verticies) * self.percentage )
    coordsRemaining += coordsRemaining % 2
    partsToDraw = coordsRemaining // 2
    self.vertex_list.resize(partsToDraw)
  def update(self, percentage):
    delta = min(max((percentage - self.percentage ) / 30, -0.01), 0.01)
    if (fabs(delta) < 0.00001):
      self.percentage = percentage
    else:
      self.percentage = self.percentage + delta
    self.percentage = min(max(self.percentage, 0), 1)
    self.__slice_points()
  def draw(self):
    pass
  def select(self, percentage):
    return percentage
