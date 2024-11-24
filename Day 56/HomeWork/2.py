def func():
    new_arr = []
    r_f = int(input("f: "))
    r_l = int(input("l: "))
    for i in range(r_f, r_l):
        new_arr.append(i)
        
    sorted_arr = []
    for j in range(1, len(new_arr), 2):
        sorted_arr.append(new_arr[j])
        
    return sorted_arr

if __name__ == '__main__':
    print(func())