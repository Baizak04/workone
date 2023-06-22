my_tuple = ()
print(type(my_tuple))

my_list = []
print(type(my_list))

my_information = list(("Dionysia",27,True,"Lemonaki",7,"Python",False))
print(my_information)
print(type(my_information))

# 4)
information = ("Jimmy",50,True,"Kate",50)
print(information)
print(type(information))

# 5)
my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False,27,"Python",27]
len(my_information)

# 6)
front_end = ("html","css","javascript")
content,styling,interactivity = front_end
print(content)

# 7)
names = ("Jimmy","Timmy","John","Kate")
print(names[2])
print(type(names))

# 8)
programming_languages = ["Python","JavaScript","Java","C"]
print(programming_languages[0])

# 9)
programming_languages = ["Python","JavaScript","Java","C"]
programming_languages[2] = "Go"
print(programming_languages)

# 10)
programming_languages = ["Python","JavaScript","Java","C"]
programming_languages.append("C++")
print(programming_languages)

# 11)
names = ["Cody","Dillan","James","Nick"]
names.insert(2, "AA")
print(names)

# 12)
programming_languages = ["Python","JavaScript"]
more_programming_languages = ["Java","C"]
programming_languages.extend(more_programming_languages)
print(programming_languages)

# 13)
programming_languages = ["Python", "JavaScript", "Java", "C"]
programming_languages.remove("Python")
print(programming_languages)

# 14)
programming_languages = ["Python", "JavaScript", "Java", "C"]
programming_languages.pop()
print(programming_languages)