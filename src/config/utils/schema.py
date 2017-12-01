from jsonschema import validate

# Make each schema contain ONLY the values shown, and all of theem
def strict(schema):
  if (schema['type'] == 'object'):
    required = []
    for k, b in schema['properties'].items():
      required.append(k)
      #  schema['properties'][k] = strict(schema['properties'][k])
    schema['required'] = required
    schema['additionalProperties'] = False
  return schema

# helper for writing objects
def object(obj):
  return {
    'type': 'object',
    'properties': obj
  }
# helper for writing arrays
def array(item):
  return {
    'type': 'array',
    'items': item
  }

# Primitive Types
integer = { 'type': 'integer' }
string = { 'type': 'string' }
color = {
  'type': 'array',
  'items': dict(integer, **{'minimum': 0, 'maximum': 255}),
  'minItems': 3,
  'maxItems': 3
}

# Json Schemas

# used to configure the screen type
screen = strict(object({
  'width': integer,
  'height': integer,
  'num_columns': integer,
  'refresh_rate': integer
}))

# the 'design' that the animator classes have to pull from
theme = strict(object({
  'theme_id': string,
  'title': string,
  'color_pallete': strict(object({
    'primary': color,
    'accent': color,
    'dull': color
  })),
  'images': strict(object({
    'wide_needle': string,
    'background': string,
    'half_circle': string
  }))
}))

# the chosen animator classes that will be drawn
animatorInstances = array(
  strict(object({
    'animator_id': string,
    'title': string,
    'column': dict(integer, **{ 'minimum': 0, 'maximum': 12 }),
    'color_override': object({
      'primary': color,
      'accent': color,
      'dull': color
    }),
    'select': array(
      strict(object({
        'serial_key': string
      }))
    )
  }))
)

# info about the serial data according to their id
serialUnits = {
  'type': 'object',
  'patternProperties': {
    '.*': strict(object({
      'unit': string,
      'max': integer,
      'min': integer
    }))
  }
}

schemas = {
  'screen': screen,
  'theme': theme,
  'animator-instances': animatorInstances,
  'serial-units': serialUnits
}

def validateJson(json, name):
  validate(json, schemas[name])
