guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("Too low")
    elif number == guess_me:
        print("Found it!")
        break
    elif number > guess_me:
        print("Oops!")
        break
    number += 1