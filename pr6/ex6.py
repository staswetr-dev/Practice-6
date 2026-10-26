point_a = (2, 5)
point_b = (8, 3)
point_c = (4, 9)

print(point_a)
print(point_b)
print(point_c)

distance_ab = ((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)**0.5
print(distance_ab)

highest_point = point_a
for p in [point_b, point_c]:
    if p[1] > highest_point[1]:
        highest_point = p

print(highest_point)