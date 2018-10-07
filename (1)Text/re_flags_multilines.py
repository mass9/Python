#The multiline floag controsl how the patterns matching code processes annchoring instructions for text containing newline characters.

import re

text = 'This is some text -- with punctuation \nA second line.'
pattern = r'(^\W+)|(\w+\S*$)'
single_line= re.compile(pattern)
multiline= re.compile(pattern, re.MULTILINE)

print('Text:\n {!r}'.format(text))
print('Pattern: \n {}'.format(pattern))
print('Single Line: ')
for match in single_line.findall(text):
    print(' {!r}'.format(match))
print('Multiline :')
for match in multiline.findall(text):
    print(' {!r}'.format(match))
