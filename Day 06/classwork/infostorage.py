import os

class user:
    age = None
    name = None
    last_name = None
    email = None

userinfo = user()

# no error checking didn't had time

print("Info storage")
age = int(input("Age: "))
name = input("Name: ")
last_name = input("Last Name: ")
email = input("Email: ")

userinfo.age = age
userinfo.name = name
userinfo.last_name = last_name
userinfo.email = email

os.system('cls')

print("User Information Stored:")
print(f"Age: {userinfo.age}")
print(f"Name: {userinfo.name}")
print(f"Last Name: {userinfo.last_name}")
print(f"Email: {userinfo.email}")