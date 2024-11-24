def func():
    new_arr = []
    r_f = int(input("f: "))
    r_l = int(input("l: "))
    for i in range(r_f, r_l):
        new_arr.append(i)
     
    l = 0   
    for j in range(1, len(new_arr), 2):
        if l < len(new_arr) and j < len(new_arr):
            new_arr[l], new_arr[j] = new_arr[j], new_arr[l]

        if l < len(new_arr) - 1:
            l = 0
            l += (j + 1)
        
    return new_arr

if __name__ == '__main__':
    print(func())