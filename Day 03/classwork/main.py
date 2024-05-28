# working with 2 integer
# start

def add(fn, sn):
    result = fn + sn
    print(result)     

def subtract(fn, sn):
    result = fn - sn
    print(result)

def multiple(fn, sn):
    result = fn * sn
    print(result) 

def divide(fn, sn):
    result = fn / sn
    print(result)  

def start():
    print("Welcome to simple calculator")
    fn = int(input("First num: " ))

    sn = int(input("Second num: "))

    print("1) add 2) subtract 3) multiple 4) divide")
    op = int(input("choose type of op: " ))

    match op:
        case 1:
            add(fn, sn)
        case 2:
            subtract(fn, sn)
        case 3:
            multiple(fn, sn)
        case 4:
            divide(fn, sn)
        case _:
            print("Invalid input")

start()