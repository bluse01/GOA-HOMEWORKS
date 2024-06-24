import os

def check_file():
    file_store = []

    path = "C:/Users/Pulling 11 g s/source/repos/GOA_HOMEWORK"
    dir_list = os.listdir(path)

    if not dir_list:
        print("Path not found!")
        return 1

    for i in range(100):
        file = "Day " + str(i)
        for i in dir_list:
            if file == i:
                file_store.append(i)

    return file_store

def makedir():
    file = check_file()
    last_element = file[-1]
    
    prefix, number_str = last_element.split()
    number = int(number_str)

    new_number = number + 1
    new_element = f"{prefix} {new_number}"

    path = f"C:/Users/Pulling 11 g s/source/repos/GOA_HOMEWORK/{new_element}"
    sidedir_classwork = f"C:/Users/Pulling 11 g s/source/repos/GOA_HOMEWORK/{new_element}/ClassWork"
    sidedir_homework = f"C:/Users/Pulling 11 g s/source/repos/GOA_HOMEWORK/{new_element}/HomeWork"

    if not os.path.exists(path):
        os.makedirs(path)

    if not os.path.exists(sidedir_classwork):
        os.makedirs(sidedir_classwork)

    if not os.path.exists(sidedir_homework):
        os.makedirs(sidedir_homework)  

makedir()