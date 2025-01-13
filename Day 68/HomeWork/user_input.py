
def text_gen(string):
    return string + str(len(string) * 2)

user_inp_arr = []

while True:
    user_inp = input("INPUT: ")
    
    if user_inp in user_inp_arr:
        print("This 'input' is already saved!")
        print(f"New 'input' generated! {text_gen(user_inp)}")
        
    user_inp_arr.append(user_inp)