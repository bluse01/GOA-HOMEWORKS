
def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

my_list = [1, 2, 3, 4, 5, 6, 7 , 8, 9]

result = sum_of_even_numbers(my_list)
print(result)