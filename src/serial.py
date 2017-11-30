class SerialInfo():
  def __init__(self, id, min, max, unit):
    self.id = id
    self.min = min
    self.max = max
    self.unit = unit

def getSerialInfo():
  return {
      'rpms': SerialInfo(
        id='rpms',
        min=0,
        max=1,
        unit='RPMs'
        )
      ,
      'psi': SerialInfo(
        id='psi',
        min=0,
        max=1,
        unit='PSI'
        )

      }

from random import uniform
serialInfoDict = getSerialInfo()
index = 0
serialDataDict = {}
def getSerialData():
  keys = ['rpms', 'psi']
  global index, serialDataDict
  if (index % 10 == 0):
    index = 0
    serialDataDict = {k: uniform(serialInfoDict[k].min, serialInfoDict[k].max)
        for k in keys}
  index += 1
  return serialDataDict
