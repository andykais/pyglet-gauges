# a helper class to allow dictionary values to be accessed like so:
# x = {'a': 1}
# assert x.a == 1

class DotDict(dict):
  """dot.notation access to dictionary attributes"""
  def __init__(self, object):
    for k, v in object.items():
      if isinstance(v, dict):
        object[k] = dotdict(v)
      if isinstance(v, list):
        object[k] = list(map(
          lambda x: dotdict(x) if isinstance(x, dict) else x,
          v
        ))
    super().__init__(object)
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

def dotdict(instance):
  if isinstance(instance, dict):
    return DotDict(instance)
  elif isinstance(instance, list):
    return list(map(
      lambda x: dotdict(x) if isinstance(x, dict) else x,
      instance
    ))
  else:
    raise ValueError('needs to be a list or dict')
