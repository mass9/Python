#!/usr/bin/env python3

# Using string as safe substitute

import string

values = { 'var': 'foo' }

t=string.Template("$var is here but $missing is not provided")

try:
    print('substitute():   ', t.substitute(values))
except KeyError as err:
    print('ERROR: ', str(err))

print('safe_substitute() : ',t.safe_substitute(values))
