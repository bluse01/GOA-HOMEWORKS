def main():
    move = ["rock", "paper", "scissors"]
    
    while True:
        user1_input = input("p1, rock, paper, or scissors: ")
        user2_input = input("p2, rock, paper, or scissors: ")
        
        if user1_input not in move and user2_input not in move:
            print("invalid move!")
            break
        
        if user1_input == user2_input:
            print("Tie!")
        elif (
            (user1_input == "rock" and user2_input == "scissors") or
            (user1_input == "paper" and user2_input == "rock") or
            (user1_input == "scissors" and user2_input == "paper")
        ):
            print("p1 win!")
        else:
            print("p2 win!")
            
main()