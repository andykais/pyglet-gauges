# Requirements
- `python3`
- `virtualenv`

# Setup
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Development
all subsequent times using the project, just rely on these commands

`roundup.sh` script contains convenience methods to run the project:
- `run` start the gui
- `watch` restart the gui every time a file in src changes
- `clean` remove pycache, virtualenv files
