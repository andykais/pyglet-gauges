import cairocffi as cairo
import io
import pyglet
from math import cos, sin, pi

def cairoSurfaceToPygletImageData(surface):
  bytesEncoder = io.BytesIO()
  surface.write_to_png(bytesEncoder)
  return pyglet.image.load('text.png', file=bytesEncoder)
  #  return pyglet.image.ImageData(
      #  surface.get_width(),
      #  surface.get_height(),
      #  'RGB',
      #  surface.get_data(),
      #  )

from random import random
def move_to(context, curveFunc, points):
  context.set_source_rgba(random(),random(),random(),1)
  x, y = curveFunc(points[0], points[1])
  context.fill()
  context.move_to(x, y)
def line_to(context, curveFunc, points):
  x, y = curveFunc(points[0], points[1])
  context.line_to(x, y)
def curve_to(context, curveFunc, points):
  x1, y1 = curveFunc(points[0], points[1])
  x2, y2 = curveFunc(points[2], points[3])
  x3, y3 = curveFunc(points[4], points[5])
  context.curve_to(x1, y1, x2, y2, x3, y3)
def close_path(context, _1, _2):
  context.close_path()

warpCases = {
  cairo.PATH_MOVE_TO: move_to,
  cairo.PATH_LINE_TO: line_to,
  cairo.PATH_CURVE_TO: curve_to,
  cairo.PATH_CLOSE_PATH: close_path
  }

def warp(context, curveFunc):
  first = True
  context_paths = context.copy_path()
  if (context_paths[0][0] != cairo.PATH_MOVE_TO):
    raise 'unexpected first val'

  context.new_path()
  for (type, points) in context_paths:
    warpCases[type](context, curveFunc, points)

def spiral(x, y, width, height):

  theta0 = -pi * 3 / 4
  theta = x / width * pi * 2 + theta0
  radius = y + 200 - x/7
  xnew = radius*cos(theta)
  ynew = radius*sin(-theta)
  return [xnew + width/2, ynew + height/2]

def curl(x, y, width, height, text_width, text_height):
  xn = x - text_width/2
  # yn = y - text_height/2
  xnew = xn
  ynew = y + xn ** 3 / ((text_width/2)**3) * 70
  return [xnew + width/2, ynew + height*2/5]

def generateTextImage():
  print('yeah sure')
  width, height = 500, 500
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
  #  surface = cairo.ImageSurface(cairo.FORMAT_A8, 300, 200)
  context = cairo.Context(surface)
  #  with context:
      #  context.set_source_rgba(0,0,0,0)
      #  context.paint()
  # Restore the default source which is black.
  context.move_to(200, 100)
  context.set_font_size(20)
  context.set_source_rgba( 1,1,1,1)
  #  context.arc(50, 50, 50, 0, 10)
  #  context.curve_to(0,0,50,200,10,100)
  context.new_path()
  context.move_to(0,0)
  context.set_source_rgba( 1,1,1,1)
  context.text_path('hello from cairo')
  warp(context,
      lambda x, y: spiral(x, y, width, height)
      )
  context.fill()
  context.move_to(0, 300)
  extents = context.text_extents("I am curly")
  print(extents)
  warp(context,
      lambda x, y: curl(x, y, 20, 20, extents[2], extents[3]))
  context.fill()
  #  context.curve_to(0,0,20,20,100,100)
  #  context.arc(90,50, 100, 90, 120)
  #  context.arc(100, 100, 80, 0, 2*math.pi)
  #  context.set_line_width(3)
  #  context.set_source_rgb(0.5, 0.0, 0.0)
  #  context.stroke()
  #  context.rotate(-0.5)
  #  extents = context.text_extents(u'Hi from my ass')
  #  context.show_text(u'Hi from cairo!')

  return cairoSurfaceToPygletImageData(surface)
  #  return surface.write_to_png(Image.fromstring)
  #  surface.write_to_png('example.png')


def textArc(text, radius, clockwise=True, start_angle=0, stop_angle=180):
  words = text.split()
  print(words)
