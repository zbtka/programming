import math

radius = 42

area = math.pi * radius ** 2
rounded_area = round(area, 4)
print(rounded_area)

point_1 = (23, 34)

distance_1 = math.sqrt(point_1[0] ** 2 + point_1[1] ** 2)
is_inside_1 = distance_1 <= radius
print(is_inside_1)

point_2 = (30, 30)

distance_2 = math.sqrt(point_2[0] ** 2 + point_2[1] ** 2)
is_inside_2 = distance_2 <= radius
print(is_inside_2)
