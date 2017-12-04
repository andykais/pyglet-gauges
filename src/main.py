from config.utils import environment
environment.set(__file__)

import pyglet
from serial import getSerialData
from view import AnimatorManager
from config.utils.access import screen

# double_buffer & sample_buffers are default values
# sample_buffer & samples pertain to antialiasing
config = pyglet.gl.Config(double_buffer=True, depth_size=24, sample_buffers=1, samples=4)
window = pyglet.window.Window(screen.get().width, screen.get().height, config=config, resizable=False) 
environment.use_in_development_only(lambda: window.set_location(5, 928))
AnimatorManager.set()

print(pyglet.gl.glGetString(pyglet.gl.GL_VERSION))

def update(dt):
  serialData = getSerialData()
  AnimatorManager.update(serialData)

@window.event
def on_draw():
  window.clear()
  AnimatorManager.draw()

pyglet.clock.schedule_interval(update, 1/screen.get().refresh_rate)
pyglet.app.run()
