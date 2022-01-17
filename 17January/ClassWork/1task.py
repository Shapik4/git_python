while True:
    name = input("Введите имя:")
    surname = input("Введите фамилию:")
    out = input("Не хотите ли Вы выйти ?")
    if out == "хватит":
        break
    print(f"Привет, {name} {surname}. Я очень рад тебя видеть! Меня зовут BOT")
