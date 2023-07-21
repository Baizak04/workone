while True:
    arument1 = input("Введите первое число: ")
    arument2 = input("Введите второе число: ")
    arument3 = input("Выберите действие: ")
    
    statement = "print({} {} {})".format(arument1, arument3, arument2)
    
    try:
        eval(statement)
    except:
        print("Уппс что то не так")