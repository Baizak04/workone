def check(prices, tip=10):
    sum_one = sum(prices)
    total = sum_one * (100 + tip) / 100
    return total


check_result = check([100, 300, 500], 0)
print(check_result)

def new_sum(*nums):
    sum = 0
    
    for num in nums:
        sum += num
        
    return sum


print(new_sum(1, 2, 34, 56))


# программа взять самый длинное слово - the program to take the longest word
def longest_word(*words):
    lender = ""
    
    for word in words:
        if len(word) > len(lender):
            lender = word
        
    return lender


print(longest_word("Ретро", "Скрам", "Достопримечательность"))


# Определение самой длинной список
def longest_list(*lists):
    lender = []
    
    for list in lists:
        if len(list) > len(lender):
            lender = list
        
    return lender


print(longest_word([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]))


# Программа для удаление препинания
def remove_from_string(string, *symbols_to_remove):
    for symbol in symbols_to_remove:
        string = string.replace(symbol, "")
        
    return string


print(remove_from_string("Смотри, можно удалить все знаки препинания сразу?", "?", "!", ","))
            

# Создать функцию которая вычисляет среднее и возвращает его округленным до первого знака
def avg(*nums):
    count = len(nums)
    nums_sum = sum(nums)
    
    return round(nums_sum / count, 1)


print(avg(1, 2, 3, 10, 4, 5))


