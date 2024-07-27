
def main():
    num = int(input("INPUT num: "))
    mult = int(input("INPUT mult: "))

    for i in range(1, num + 1):
        result = mult * i
        print(str(mult) + " * " + str(i) + " = " + str(result))

main()