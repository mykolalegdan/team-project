contacts = []  # Наш список для зберігання

while True:
    action = input("\n1 - Додати, 2 - Список, 0 - Вихід: ")

    if action == "1":
        name = input("Ім'я: ")
        contacts.append(name)
        print("Збережено!")

    elif action == "2":
        print("Ваші контакти:", contacts)

    elif action == "0":
        break