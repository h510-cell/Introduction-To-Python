import random
number = random.randint(1,9)
guess = input()
guess = int(guess)

if guess < number:
    print('Your guess is just to near.')

if guess > number:
    print('Your guess has went behind.')

if guess == number:
    break

 if guess == number:
     print("Yippe! You got the number")