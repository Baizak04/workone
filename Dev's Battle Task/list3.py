# lst = list('alan wake')
# print(lst.index('a', 0, 5))

# lst = [1, 2, 3] * -1
# lst *= 2
# print(lst)

# lst = [i * 2 for i in 'pip']
# print(lst)

# lst = [2, 0, 2, 2]
# del lst[:-2:]
# print(lst)

# a = [1, 2, 3]
# a.extend([2, 6])
# print(a)

# lst = [5]
# lst *= 3
# lst[0] = 0
# lst[2] = 10
# print(sum(lst))

# lst1 = [0, 1, 2]
# lst2 = lst1.append([3])
# print(len(lst2))

# f_lst = [1, 2, 3]
# s_lst = f_lst
# f_lst.pop(0)
# s_lst.append(4)
# print(f_lst)

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print([arr[i][i] for i in range(len(arr))])