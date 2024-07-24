
def return_vowels(string):
    vowels_matches = ["a", "e", "i", "o", "u", "y"]

    my_count = 0
    for char in string:
        for match in vowels_matches:
            if char == match:
                my_count += 1
                
    print(my_count)

string = input("INPUT: ")

return_vowels(string)