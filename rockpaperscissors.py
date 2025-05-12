import random

user_score = 0
comp_score = 0
ties = 0

name = input("Enter your name here: ")
print("""
Winning Rules:
1. Paper vs Rock --> Paper
2. Rock vs Scissors --> Rock
3. Scissors vs Paper --> Scissors""")

print("Choices are:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

while True:
    choice = int(input("Enter your choice (1-3): "))
    
    if choice < 1 or choice > 3:
        print("Please enter a valid input (1-3).")
        continue
    
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"
    
    print("Your choice is", user_choice)
    
    computer = random.randint(1, 3)
    
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    
    print("Computer's choice is", comp_choice)
    
    if (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Paper"):
        print(user_choice, "wins")
        result = "User"
    elif user_choice == comp_choice:
        print("It's a tie")
        result = "Tie"
    else:
        print(comp_choice, "wins")
        result = "Computer"
    
    if result == "Tie":
        ties += 1
    elif result == "User":
        user_score += 1
    else:
        comp_score += 1
    
    print("Scores are:")
    print(name, "'s score is", user_score)
    print("Computer's score is", comp_score)
    print("Ties are", ties)
    
    repeat = input("Do you want to play again? (Yes/No): ")
    if repeat.lower() != "yes":
        break

print("Game over!")
print('Thanks for playing!!!')