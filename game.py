"""A number-guessing game."""

import random 

# greet player
print('Welcome to the number-guessing game!')
# get player name
name = input('What is your name? > ')

# choose random number between 1 and 100
rand_num = random.randint(1,99)
# print (rand_num)
guess = 0
num_guesses = 1
# repeat forever:
while guess != rand_num:
    while True:
        try:
            guess = int(input('Guess a number between 1 and 100 > '))
            break
        except ValueError:
            print('Oops. That\'s not a valid number')
            num_guesses += 1
#     get guess
#     if guess is incorrect:
    if 0 < guess and guess < rand_num:
        print ('too low!')
    elif guess > rand_num and guess < 100:
        print ('too high!')
#         give hint
#         increase number of guesses
    elif guess <= 0 or guess >= 100:
        print('that number is not in the valid range') 
    else:
        print(f'Congratulations! You won in {num_guesses} guesses.')
    num_guesses += 1
#     else:
#         congratulate player