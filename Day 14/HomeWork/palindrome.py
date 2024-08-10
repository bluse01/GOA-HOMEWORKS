
def main():
    print("Input a string that read same backwards")
    string = input("INPUT: ")

    string_list = []
    for i in string:
        string_list.append(i)
    string_list.reverse()
    revesed_string = "".join(string_list)

    if string == revesed_string:
        print("This word is a palindrome!")
    else:
        print("This word is not palindrome!")

main()