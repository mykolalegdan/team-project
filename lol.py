contacts = []

while True:
    action = input("\n1-Додати, 2-Список, 3-Видалити, 0-Вихід: ")
    if action == "1":
        name = input("ПІБ: ")
        phone = input("Номер: ")
        contacts.append({"name": name, "phone": phone})
        print("Додано!")

    elif action == "2":
        for c in contacts:
            print(f"{c['name']}: {c['phone']}")

    elif action == "3":
        name = input("Кого видалити? (ПІБ): ")
        contacts = [c for c in contacts if c['name'] != name]
        print("Оновлено.")

    elif action == "0":
        break
