import re

"""
This is simple match for expression
"""

pattern = 'this'
text = 'Does this text match the pattern?'

match= re.search(pattern, text) 
s = match.start()
e= match.end()

print("Found: ->",match.re.pattern,"<-\nin ->",match.string,"<-\n From ",s, "to",e, '("%s")'%text[s:e])
