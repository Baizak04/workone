def first_int(number: int): 
    # внутри скобки это аргумент, если передать еще аргумент то указывать через запятую
    # Первая строка в функции называется заголовком (header) весь остальной ее код называется телой (body)
    print(number + 1)
    
    
# first_int(2)

#  Alt + ↓ / ↑ — переместит строку с курсором вверх или вниз, в зависимости от комбинации клавиш.

def repeat_int(number_one: int):
    first_int(number_one)
    first_int(number_one)
    
    
repeat_int(2 * 3)


def first_str(world: str):
    print(world)
    
def repeat_str(world_one: str):
    return first_str(world_one)


repeat_str('Baizak ' * 2)



def cat(part1: str, part2: str):
    cat_print = part1 + part2
    return cat_print


cat_one = 'Тили-тили '
cat_two = 'Трали-вали'
print(cat(cat_one, cat_two))