import math

def count_area(x, y=0, z=0):
    if x and y and z:
        s = (x + y + z) / 2
        return  math.sqrt(s * (s - x) * (s - y) * (s - z))
    if x and y and z == 0:
        return x * y
    if x and y == 0 and z == 0:
        return math.pi * pow(x, 2)

print(count_area(3, 4, 5))