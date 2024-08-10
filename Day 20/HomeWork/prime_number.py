
def get_prime_number(num):
    if num < 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            print("This number is not a prime number!")
            return False
        else:
            print("This is a prime number!")

val = 3
get_prime_number(val)