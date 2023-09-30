# my_languages = {'Python', 'Go', 'Java'}
# my_languages.add('Swift')
# print(my_languages)

my_language = {'Python', 'Go', 'Java'}
removed_language = my_language.pop()
print(removed_language)

my_language = {'Python', 'Go', 'Java'}
my_language.discard('Go')
print(my_language)

# my_language = {'Python', 'Go', 'Java'}
# my_language.remove('Java')
# print(my_language)

# backend_languages = {'Python', 'Go', 'Java', 'PHP', 'C++'}
# frontend_languages = {'HTML', 'Css', 'JavaScript'}
# my_languages = backend_languages.union(frontend_languages)
# print(my_languages)


# backend_languages = {'Python', 'Go', 'Java', 'PHP', 'C++', 'HTML'}
# frontend_languages = {'HTML', 'Css', 'JavaScript'}
# my_languages = backend_languages.intersection(frontend_languages)
# print(my_languages)

# backend_languages = {'Python', 'Go', 'Java', 'PHP', 'C++', 'HTML'}
# frontend_languages = {'HTML', 'Css', 'JavaScript'}
# my_languages = backend_languages.difference(frontend_languages)
# print(my_languages)

# backend_languages = {'Python', 'Go', 'Java', 'PHP', 'C++', 'HTML'}
# frontend_languages = {'HTML', 'Css', 'JavaScript'}
# my_languages = backend_languages.issubset(frontend_languages)
# print(my_languages)