
def sort_ls(lst):    
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= len(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
                
    return lst

    

my_list = ['python','cat', 'running', 'code', 'glass', 'future']

print(sort_ls(my_list)) 