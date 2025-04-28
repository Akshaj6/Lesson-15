import random
number = random.randint(1,10)
playing = True
print("Welcome to the number guessing game!")
print("Please choose a number from 1 to 10. The game ends when you choose the correct number.")
while playing:
    guess = int(input("Enter a number : "))
    if number == guess:
        print("Congratulations! You won!!")
        playing = False
        break
    else:
        print("Sorry, that's the wrong answer. Please try again")