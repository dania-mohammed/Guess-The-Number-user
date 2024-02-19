import random

def guess(x):
    random_number = random.randint(1,x)


    user_geuss = 0
    while user_geuss != random_number:
        user_geuss = int(input(f"Guess the number btween 1 and {x} "))
        if user_geuss > random_number:
            print("That is too high , guess again ")
        elif user_geuss < random_number:
            print("That is too small, guess again ")
    print (f"congrat you guess it. it's {random_number}")

guess(10)
