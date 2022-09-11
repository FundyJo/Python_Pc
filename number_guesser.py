
import random

while True:
    try:
        top_of_range = int(input("Schreibe eine Zahl!: "))
        break
    except Exception:
        continue

random_number = random.radiant(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guesses = input("Entscheide dich!: ")
    if user_guesses.isdigit():
        if user_guesses: int(user_guesses)
    else:
        print("Schreibe bitte eine Nummer. ")
        continue

    if user_guesses == random_number:
        print("Du hast die Zahl gefunden!")
        break
    elif user_guesses > random_number:
        print("Du bist über der Zahl!")
    else:
        print("Du bist unter der Zahl!")

print("Du hast die Zahl nach", guesses, "gefunden!")
