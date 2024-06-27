
def main():
    x = 50

    for num in range(x + 1):
        if num > 1:
            for h in range(2, num):
                if num % h == 0:
                    break
            else:
                print(num)

main()