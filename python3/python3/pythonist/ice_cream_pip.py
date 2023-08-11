from icecream import ic


def square_of(num):
    return num * num


ic(square_of(2))
ic(square_of(3))
ic(square_of(4))


# 2)
my_dict = {
    'имя': 'Артем',
    'возраст': 33
}
ic(my_dict['имя'])

# 3)
def check_user(username):
    if username == 'Максим':
        # сделать что-то
        ic()
    else:
        # сделать что-то
        ic()
check_user('Максим')
check_user('Денис')