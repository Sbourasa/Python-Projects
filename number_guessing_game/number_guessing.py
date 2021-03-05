import random

#game main menu / difficulty selector
print("Please select difficulty")
print(" 1 : Easy (10 guesses)")
print(" 2 : Medium (7 guesses)")
print(" 3 : Hard (5 guesses)")

difficulty = int(input())

the_number = random.randint(1,100)

number_of_guesses = 10

if difficulty == 2:
    number_of_guesses = 7
elif difficulty == 3:
    number_of_guesses = 5
    
print("I've got a number 1 - 100, can you guess it?")
i = 0
while i < number_of_guesses:

    print("~~ Guess #", (i+1), "of", number_of_guesses, "~~")
    guess = int(input("Enter a number: "))

    if guess == the_number:
        print("Congratulations, you've guessed", the_number, "in", (i+1), "attempts!")
        break

    elif guess > the_number and i != (number_of_guesses-1):
        print("Wrong! The number is less than", guess)

    elif guess < the_number and i != (number_of_guesses-1):
        print("Wrong! The number is greater than", guess)

    if i == (number_of_guesses-1):
        print("Game Over! The number was", the_number)

    i += 1