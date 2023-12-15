# 1)
def test(a, b='str', c='str2'):
    return (a, b, c)


print(test(100))


# 2)
def test(a, b='str', c='str2'):
    return (a, b, c)


print(test(100, b='12'))

# 3)
def test_two(a, b, *, c=None):
    return (a, b, c)

print(test_two(10, 12))





