grades = [11, 8, 12, 3, 10, 7, 2, 9, 10, 6]

print(grades)

print(max(grades))
print(min(grades))

average = sum(grades) / len(grades)
print(average)

high_grades_count = 0
for grade in grades:
    if grade >= 10:
        high_grades_count += 1
print(high_grades_count)

low_grades = []
for grade in grades:
    if grade < 4:
        low_grades.append(grade)
print(low_grades)