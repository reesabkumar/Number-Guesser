import random
from secrets import randbelow

random_number=input("Enter a digit to generate number: ")

if random_number.isdigit():
    random_number = int(random_number)

    if random_number <=0:
        print("Enter a number greater than 0 ")
        quit()
else:
    print("Only number are supported please enter a number")
    quit()

random_number = random.randint(0, random_number)
#print(random_number)
guesses=0
while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please try number next time. ")
        continue

    if user_guess == random_number:
        print("You Got it")
        break
    else:
        if user_guess > random_number:
            print("Your guess is greater than number")
        else:
            print("Your guess is less than number")

print("You got in it",guesses,"times")

 