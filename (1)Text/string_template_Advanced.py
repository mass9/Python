#!/usr/bin/env python

import string

class MyTemplate(string.Template):
    delimiter = "%"
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
Delimiter : %%
Replaced  : %with_underscore
Ignored   : %notunderscore
'''

d = {
    'with_underscore' : 'replaced',
    'notunderscored'  : 'not replaced',
        
        }

t= MyTemplate(template_text)
print('Modified ID pattern: ')
print(t.safe_substitute(d))
