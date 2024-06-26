import os

path = "C:/Users/Pulling 11 g s/source/repos/GOA_HOMEWORK"

def dirlist():

    dir_list = os.listdir(path)
    filter_dir = []
    last_string = None
    
    for i in dir_list:
        if "Day " in i:
            filter_dir.append(i)

    return filter_dir

def make_sidedir(path):
    new_path_sidedir = [f"{path}/ClassWork", f"{path}/HomeWork"]

    for subdir in new_path_sidedir:
        if not os.path.exists(subdir):
            os.makedirs(subdir)

def makedir():
    filter_dir = dirlist()
    last_element = filter_dir[-1]

    prefix, num = last_element.split()

    def low_dir():
        num1, num2 = [char for char in num]
        new_num = int(num2) + 1
        new_num = str(num1) + str(new_num)
        new_string = prefix + new_num
        new_path = f"{path}/{new_string}"

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        make_sidedir(new_path)

    def high_dir():
        new_num = int(num) + 1
        new_string = prefix + " " + str(new_num)
        new_path = f"{path}/{new_string}"
        
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        make_sidedir(new_path)

    if int(num) < 9:
        low_dir()

    if int(num) >= 9:
        high_dir()
    

makedir()