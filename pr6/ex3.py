numbers = [1, 4, 7, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(even_numbers)
print(len(even_numbers))

print(odd_numbers)
print(len(odd_numbers))

print(sum(even_numbers))