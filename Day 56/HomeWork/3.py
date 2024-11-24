
def func():
    new_arr = []
    for i in range(0, 11):
        n = int(input("n: "))
        print(f"n: {n} | th: {i}")
        new_arr.append(n)
        
    result_arr = []
    for j in range(0, len(new_arr)):
        result_arr.append(new_arr[j] * 2)
        
    return result_arr

if __name__ == '__main__':
    print(func())