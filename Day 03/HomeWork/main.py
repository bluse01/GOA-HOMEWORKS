
def operations(num1, num2):
    op_list = [lambda a, b : a + b, lambda a, b : a - b, lambda a, b : a * b, lambda a, b : a / b,]

    for i in op_list:
        print(i(num1, num2))


num1 = 5 
num2 = 7

operations(num1, num2)