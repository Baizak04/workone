def extendList(val, list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
print (f"list1 = {list1}")
print (f"list2 = {list2}")
print (f"list3 = {list3}")

# Многие могут ошибочно предположить, что list1 будет равен [10], а list3 будет равен ['a'], думая, что всякий раз при вызове функции extendList аргумент list будет равен значению по умолчанию []. Однако, в действительности новый пустой список по умолчанию создается только один раз при определении функции. И затем этот список последовательно используется всякий раз, когда функция вызывается без второго аргумента. Это происходит потому, что значения по умолчанию вычисляются при определении функции, а не при ее вызове. Таким образом, list1 и list3 имеют дело с одним и тем же списком по умолчанию, в то время как list2 использует пустой список, переданный ему во втором аргументе.