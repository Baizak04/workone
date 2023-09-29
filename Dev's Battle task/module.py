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