days = ("Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя")

print(days[0])
print(days[-1])

print(days[:5])

if "Середа" in days:
    print("Є у кортежі")
else:
    print("Немає у кортежі")

print(len(days))

try:
    days[0] = "Новий день"
except TypeError:
    print("Помилка: кортеж незмінний")