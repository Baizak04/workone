import math
import datetime
print(math.factorial(5))
print(datetime.datetime.now())

import time
# seconds = time.time()
# print(seconds)
# local = time.ctime(seconds)
# print(local)


seconds_two = time.time()

result = time.localtime(seconds_two)
print(result.tm_year)
print(result.tm_mday)
print(result.tm_hour)
print(result.tm_min)
print(result.tm_sec)


