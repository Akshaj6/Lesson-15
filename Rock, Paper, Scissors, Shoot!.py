import random
options = ["Rock", "Paper" and "Scissors"]
user_choice = input("Chosse Rock, Paper or Scissors : ")
computer_choice = random.choice(options)
print("You chose", user_choice)
print("Computer chose", computer_choice)
if user_choice == computer_choice:
    print("Its a tie!!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes Scissors! You win!!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers Rock! You win!!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts Paper! You win!!")
else:
    print("You lose.")