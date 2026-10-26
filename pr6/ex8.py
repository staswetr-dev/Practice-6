products = [
    ("Ноутбук", 25000),
    ("Мишка", 800),
    ("Клавіатура", 1500),
    ("Монітор", 7000),
    ("Навушники", 2200)
]

for name, price in products:
    print(f"{name}: {price}")

expensive_product = products[0]
for item in products:
    if item[1] > expensive_product[1]:
        expensive_product = item
print(expensive_product[0])

total_sum = 0
for item in products:
    total_sum += item[1]
print(total_sum)

for item in products:
    if item[1] > 2000:
        print(item[0])