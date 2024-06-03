import os

class user:
    Name = None
    Password = None

# if string more then 3 and not empty = Good/True
def string_check(string):
    if len(string) < 3:
        print("Username to short")
        exit()
    
    if string.strip():
        None
    else:
        print("String is empty")
        exit()

def save_user(username, password):
    data = open("data.txt","a+")
    data.write(f"{username},{password}\n")
    data.close()

def verify_user(username, password):
    data = open("data.txt","r")

    for line in data:
        stored_username, stored_passowrd = line.strip().split(",")
        if stored_username == username and stored_passowrd == password:
            data.close()  
            return True
        
    data.close()      
    return False

def sign_in():
    os.system("cls")
    print("\nPlease Sign in")

    signuser = user()

    username = input("Username: ")
    string_check(username)
    signuser.Name = username

    userpassword = input("Password: ")
    string_check(userpassword)
    signuser.Password = userpassword

    save_user(username, userpassword)
    print("User signed in successfully")

def log_in():
    os.system("cls")
    print("\nPlease Login in")

    username = input("Username: ")

    userpassword = input("Password: ")

    if verify_user(username, userpassword):
        print("Login successful")
    else:
        print("Invalid info")

def main():
    print("1) Signin\n2) Login")
    
    match int(input("INPUT: ")):
        case 1:
            sign_in()
        case 2:
            log_in()
        case _:
            print("Invalid input")
        
    
main()