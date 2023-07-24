def todo_list():
    tasks = []

    while True:
        print("1. Добавить задачу")
        print("2. Просмотр заданий")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Введите свой выбор: ")

        if choice == '1':
            task = input("Введите задачу: ")
            tasks.append(task)
        elif choice == '2':
            if tasks:
                print("Задачи:")
                for task in tasks:
                    print(task)
            else:
                print("Нет задач.")
        elif choice == '3':
            if tasks:
                task = input("Введите задание для удаления: ")
                if task in tasks:
                    tasks.remove(task)
                    print("Задача снята.")
                else:
                    print("Задача не найдена.")
            else:
                print("Задачи отсутствуют.")
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

todo_list()