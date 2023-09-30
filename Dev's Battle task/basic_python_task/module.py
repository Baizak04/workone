from heapq import heappush, heappop


h = []
heappush(h, (5, 'a'))
heappush(h, (7, 'b'))
heappush(h, (3, 'c'))
print(heappop(h)[1])

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
result = sum((len(d['a'] * 3), len(d['b']) * 5))
print(result)

from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
c['z'] = 10
c['w'] = 40
del c['x']
print(sum(a.values()), sum(b.values()))

from math import pi

h = 10.0
r = 2.5

circles = 2 * (pi * r**2)
side = 2 * pi * r * h
area = circles + side

print(round(area, 2))