
plus_x = lambda a : a + a
minus_x = lambda a : a - a
power_x = lambda a : a * a
div_x = lambda a : a / a

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in my_list:
    print(f"val {i}: + {plus_x(i)} , - {minus_x(i)} , * {power_x(i)} , / {div_x(i)}")