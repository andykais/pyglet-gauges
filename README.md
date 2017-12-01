# Requirements
- `python3`
- `pip install pipenv`

# Setup
```bash
pipenv install # only run this once
pipenv shell # run this every time (much like sourcing virtualenv)
```

# Development
`roundup.sh` script contains convenience methods to run the project:
- `run` start the gui
- `run:prod` start the gui in production mode (e.g. connected to a serial device)
- `watch` restart the gui every time a file in src changes
- `clean` remove pycache, virtualenv files

use `pipenv install [package]` when installing a new python package

# Architecture
The basic idea of the design is that any 'configuration' to the project is held in the json
files in the `config/` directory. Currently the only configuration files are as follows:
- `theme.json` - the images and colors that all animators pull from
- `animator-instances.json` - the animators that are chosen to be drawn to the screen
- `screen.json` - basic config for the screen like width, height, refresh_rate
- `serial-units.json` - info about the serial data being sent like min, max, units

Config files are structured based on jsonschemas: [src/config/utils/schema.py](src/config/utils/schema.py)
