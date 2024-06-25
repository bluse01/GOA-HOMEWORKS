
def main():
    fnumber = int(input("fnumber Input: "))
    snumber = int(input("snumber input: "))

    operation = [lambda x,y: x+y, lambda x,y: x-y, lambda x,y: x/y, lambda x,y: x*y]

    for i in operation:
        print(i(fnumber,snumber))

main()