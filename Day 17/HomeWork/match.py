
def match_list(list1, list2):
    for items in my_list:
        for v in second_list:
            if items == v:
                print("Matching values in a list: "  + str(v))

my_list = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
second_list = [".py", "3.14", 5, 4, "code", 9]

match_list(my_list, second_list)