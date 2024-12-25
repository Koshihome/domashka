# 1 задание
import re
hehe = input()
nothehe = hehe.replace('н', '!')
print(nothehe)
print (len(max(re.findall(r'н+', hehe))))
