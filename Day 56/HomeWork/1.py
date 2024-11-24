
def func():
    new_arr = []
    for i in range(5):
        n = int(input("n: "))
        print(f"n: {n} | th: {i}")
        new_arr.append(n)
        
    return f"n2: {new_arr[2]}, n4: {new_arr[4]}"
    

if __name__ == '__main__':
    print(func())