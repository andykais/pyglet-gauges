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
- `watch` restart the gui every time a file in src changes
- `clean` remove pycache, virtualenv files

use `pipenv install [package]` when installing a new python package
