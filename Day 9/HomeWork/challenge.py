import os

class vec_calc:
    a: float
    b: float
    c: float

    def calc_sides(self, x, y, c) -> bool:
        if x + y > c and x + c > y and y + c > x:
            return True
        return False

def main():
    def input_func():
        a = float(input("X: "))
        b = float(input("Y: "))
        c = float(input("C: "))

        return a, b, c
    
    a, b, c = input_func()

    triangle_calc = vec_calc()
    result = triangle_calc.calc_sides(a, b, c)

    if result:
        print("triangle is valid.")
    else:
        print("triangle is not valid.")

main()
os.system("pause")