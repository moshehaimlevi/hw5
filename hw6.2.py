# start

import random

number = random.randint(1, 100)

counter: int = 1

user_attempt: int = int(input("guess the correct number"))

while user_attempt > number:

    print('too high guess again')

    counter += 1

    user_attempt: int = int(input('guess again'))

if user_attempt == number:
    print('correct')
    counter = + 1
else:
     print('too low guess again')
