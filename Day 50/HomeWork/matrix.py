
def matrix(n):
    
    new_arr = []
    for i in n:
        temp_arr = []
        for x, y in i:
            temp_arr.append(x + y)
            
        new_arr.append(temp_arr)
        
    print(new_arr)

view2d = [[1,3],[1,4]], [[4,1],[2,2]]
matrix(view2d)