from . import *

import jsonschema
types = {"function": callable, "path": isPath}
validator = jsonschema.Draft4Validator(schema, types=types)
flagsValidator = jsonschema.Draft4Validator(schema["definitions"]["compilerFlags"], types=types)
