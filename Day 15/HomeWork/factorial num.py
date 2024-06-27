
def main():
    factorial = int(input("INPUT: "))

    if factorial > 0:
        for num in range(1, factorial + 1):
            factorial *= num
            print(factorial)
    
main()