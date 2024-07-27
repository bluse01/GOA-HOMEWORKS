
def main():
    x = 100

    for num in range(x + 1):
        if num > 1:
            if num % 3 == 0 and num % 5 == 0:
                print(num)
            
main()