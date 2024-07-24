def factorial(number):
    if number < 0:
        raise TypeError("Factorial is not defined for negative numbers")
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

num = int(input("INPUT: "))
print(factorial(num))