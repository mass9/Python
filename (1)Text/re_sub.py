import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'MAke thise **bold** . Thise **too**'

print('Text: ',text)
print('Bold:', bold.sub(r'<b>\1</b>',text))
