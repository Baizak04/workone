# 1)
def test():
    return "text"


test_format = f"test(): {test()}"
print(test_format)

# 2)
text = (
    f'name: {100}',
    f'age: {25.0}'
    )

print(text)


# 3)
def test():
    return "test_result"


test_format = f'{test()=}'
print(test_format)

# 4)
print(f'{20.1:.3f}')

# 5)
value = 21.54
value_one = f'{value:.1f}'
print(value_one)