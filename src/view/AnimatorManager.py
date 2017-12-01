import pyglet
from config.utils.access import theme, animatorInstances, serialUnits

from .animators import animatorClasses

batch = pyglet.graphics.Batch()
groups = dict({
  'background': pyglet.graphics.OrderedGroup(0),
  'gauges': pyglet.graphics.OrderedGroup(1),
  'needles': pyglet.graphics.OrderedGroup(2),
  'text': pyglet.graphics.OrderedGroup(3)
})

animators = []
# TODO make set call delete() when removing old animators from batch
def set():
  global animators
  animators = []
  for gaugeData in animatorInstances.get():
    animators.append(
      animatorClasses[gaugeData['animator_id']](
        theme=theme.get(),
        column=gaugeData['column'],
        groups=groups,
        batch=batch,
        color_override=gaugeData.color_override,
        serialKeys=list(map(
          lambda object: object['serial_key'],
          gaugeData['select']
        ))
      )
    )

def draw():
  batch.draw()
