import random 

random.seed()  

number = int(random.random() * 100)

print("Enter your guess (or enter -999 to quit): ")
guessed = int(input())

while guessed != number and guessed != -999:
    print("You got it wrong")
    guessed = int(input())

print("Congratulations! You've guessed the correct number!")
