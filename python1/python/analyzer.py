# analyzer word

print("*" * 15, "Анализатор слов ", "*" * 15)
word = input("Введите слово: ")

vowels = 0
consonants = 0
vvs = ["а","о","и","е","е","э","ы","у","ю","я"]

for i in word:
    letter = i.lower()
    if letter in vvs:
            vowels += 1
    else:
        consonants += 1
        
print("Длина текста: ", len(word))
print("Гласные %i Согласные %i" % (vowels, consonants))
