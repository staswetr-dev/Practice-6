students = [
    ["Олександр", [10, 11, 9]],
    ["Марія", [12, 10, 12]],
    ["Іван", [7, 8, 9]]
]

while True:
    print("\n===== ЕЛЕКТРОННИЙ ЖУРНАЛ =====")
    print("1. Показати всіх студентів")
    print("2. Додати студента")
    print("3. Додати оцінку студенту")
    print("4. Переглянути оцінки студента")
    print("5. Показати середній бал студента")
    print("6. Видалити студента")
    print("0. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        for s in students:
            print(f"{s[0]}: {s[1]}")

    elif choice == "2":
        name = input("Ім'я: ")
        students.append([name, []])

    elif choice == "3":
        name = input("Ім'я: ")
        found = False
        for s in students:
            if s[0].lower() == name.lower():
                grade = int(input("Оцінка: "))
                s[1].append(grade)
                found = True
                break
        if not found:
            print("Студента не знайдено")

    elif choice == "4":
        name = input("Ім'я: ")
        found = False
        for s in students:
            if s[0].lower() == name.lower():
                print(s[1])
                found = True
                break
        if not found:
            print("Студента не знайдено")

    elif choice == "5":
        name = input("Ім'я: ")
        found = False
        for s in students:
            if s[0].lower() == name.lower():
                if len(s[1]) > 0:
                    print(sum(s[1]) / len(s[1]))
                else:
                    print("Оцінок немає")
                found = True
                break
        if not found:
            print("Студента не знайдено")

    elif choice == "6":
        name = input("Ім'я: ")
        found = False
        for s in students:
            if s[0].lower() == name.lower():
                students.remove(s)
                found = True
                break
        if not found:
            print("Студента не знайдено")

    elif choice == "0":
        break