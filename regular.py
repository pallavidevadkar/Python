import re
s='This is D Y patil collage'
match=re.search('collage',s)
print('start index',match.start())
print('end index',match.end())
print(match)