import random

from LoL_Characters import LoL_Characters

def dashes(secret_character):

    dash = ""

    for i in secret_character:
        if i == " ":
            dash = dash + " "
        else:
            dash = dash + "-"

    return dash
    
def upd_dashes(secret_character, dashes):

    while True:
        ind = random.randint(0, len(secret_character)-1)
        if dashes[ind] != " ":
            break

    dash = ""

    for i in range(len(secret_character)):
        if i == ind:
            dash = dash + secret_character[i]
        else:
            dash = dash + dashes[i]

    return dash

def guess(secret_character, dash):

    guess_chance = 0
    Guess = ""

    while Guess != secret_character and guess_chance < 4:

        if guess_chance > 0:
            dash = upd_dashes(secret_character, dash)
            print(dash)

        Guess = input("guess : ").lower()
        guess_chance += 1

    return Guess

def main():

    rng = random.randint(1, len(LoL_Characters))
    secret_character = LoL_Characters[rng].lower()
    
    dash = dashes(secret_character)
    print(dash)

    Guess = guess(secret_character, dash)

    if Guess == secret_character:
        print("There is a winner")
    else:
        print(f"It is {secret_character}, LOSER")

main()