import timeit
a = timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)
print(a)

# 2)
s = timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)
print(s)

# 3)
d = timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)
print(d)