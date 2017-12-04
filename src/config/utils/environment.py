
def set(base_dir):
  global production
  import os
  # decide whether this is a production run or a development run
  production = os.environ.get('PRODUCTION', False) != False

  # make sure cwd is root
  dir_path = os.path.dirname(os.path.realpath(base_dir))
  os.chdir(dir_path)
  del os

def use_in_development_only(func):
  if (not production):
    func()
def use_in_production_only(func):
  if (production):
    func()
