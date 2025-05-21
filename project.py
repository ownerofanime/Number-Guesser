import random

rnd = int(input('Please input a starting range number: '))
rnd2 = int(input('Please input an ending range number: '))
random_number = random.randint(rnd, rnd2)
random_guess = int(input(f'please guess a number between the range of {rnd} and {rnd2}: '))
while random_guess != random_number:
    if random_guess <= rnd or random_guess >= rnd2:
        int(input(f'please input a number that is in between the range!: '))
    elif random_guess < random_number:
        int(input('you need to guess the number a bit higher!: '))
    elif random_guess > random_number:
        int(input('you need to guess the number a bit lower!: '))
    else: 
        print('congratulsations! You have guessed the correct number!')

