import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path) # make sure cwd is root
import pyglet
from pyglet import gl
from animator_classes import HalfCircleWideNeedle, Background, ArcGauge
from serial import getSerialData

config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(1024, 150, config=config, resizable=False) 
window.set_location(5, 920)


batch = pyglet.graphics.Batch()
groups = dict({
  'background': pyglet.graphics.OrderedGroup(0),
  'gauges': pyglet.graphics.OrderedGroup(1),
  'needles': pyglet.graphics.OrderedGroup(2),
  'text': pyglet.graphics.OrderedGroup(3)
  })
# TODO move this step to a json config file
animators = [
  Background.animator(groups=groups, batch=batch),
  HalfCircleWideNeedle.animator(
    groups=groups,
    batch=batch,
    color=(240,0,70),
    needleColor=(0,80,100),
    serialKeys=['rpms']),
  HalfCircleWideNeedle.animator(
    column=3,
    groups=groups,
    batch=batch,
    color=(0,255,255),
    needleColor=((255,255,0)),
    serialKeys=['psi']),
  ArcGauge.animator(
    column=3,
    groups=groups,
    batch=batch,
    color=(255,255,255),
    needleColor=(255,0,0),
    serialKeys=['psi'])
  ]

def update(dt):
  serialData = getSerialData()
  for animator in animators:
    animator.update(animator.select(serialData))

@window.event
def on_draw():
  batch.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
