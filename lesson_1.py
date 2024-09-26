# 1 задание:

import math
r = int(input())
c = 2*math.pi*r
s = math.pi*(r**2)
print(round(c, 2))
print(round(s, 2))

# 2 задание:

x = 10
y = 55
print('До замены: x =', x, 'y =', y)
x = x + 45
y = y - 45
print('После замены: x =', x,'y =', y)

# 3 задание:

import math
l = int(input())
g = 9.81
t = 2 * math.pi * math.sqrt(l/g)
print(round(t, 2))