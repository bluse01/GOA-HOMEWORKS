def func():
    new_arr = []
    r_f = int(input("f: "))
    r_l = int(input("l: "))
    for i in range(r_f, r_l):
        new_arr.append(i)
        
    return new_arr[::-1]
        
if __name__ == '__main__':
    print(func())