
def main():
    print("\n\nPasswordChecker")
    password1 = input("password: ")
    password2 = input("Re-enter password: ")

    if password1 != password2:
        print("Passwords don't match!")     
    else: 
        print("Password successful saved!")

main()