students = ["Андрій", "Джон", "Максим", "Ірина", "Тарас", "Ольга", "Богдан", "Юлія"]

name_to_find = input()

found = False
for i in range(len(students)):
    if students[i].lower() == name_to_find.lower():
        print(f"Позиція: {i}")
        found = True
        break

if not found:
    print("Студента не знайдено")