from config.utils import environment
environment.set(__file__)

import pyglet
from serial import getSerialData
from view import AnimatorManager
from config.utils.access import screen

config = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(screen.get().width, screen.get().height, config=config, resizable=False) 
environment.use_in_development_only(lambda: window.set_location(5, 928))
AnimatorManager.set()

def update(dt):
  serialData = getSerialData()
  AnimatorManager.update(serialData)

@window.event
def on_draw():
  AnimatorManager.draw()

pyglet.clock.schedule_interval(update, 1/screen.get().refresh_rate)
pyglet.app.run()
