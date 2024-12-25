# 1 задание
import re
hehe = input()
nothehe = hehe.replace('н', '!')
print(nothehe)
print (len(max(re.findall(r'н+', hehe))))

# 2 задание
import re
hehe = input()
print(re.findall(r'\((.+?)\)', hehe))

# 3 задание
import re
hehe = input().lower()
print(re.findall(r'\bа\w+я\b', text))
