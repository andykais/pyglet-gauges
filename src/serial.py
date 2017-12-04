from config.utils import access, environment
from random import uniform


class SerialInfo():
  def __init__(self, id, min, max, unit):
    self.id = id
    self.min = min
    self.max = max
    self.unit = unit


index = 0
serialDataDict = {}
def getFakeSerialData():
  serialInfo = access.serialUnits.get()
  keys = serialInfo.keys()
  global index, serialDataDict
  if (index % 10 == 0):
    index = 0
    serialDataDict = {k: uniform(serialInfo[k]['min'], serialInfo[k]['max'])
        for k in keys}
  index += 1
  return serialDataDict


def getSerialDataFromDevice():
  # TODO make this return real data
  return getFakeSerialData()

def getSerialData():
  if (environment.production):
    return getSerialDataFromDevice()
  else:
    return getFakeSerialData()
