import random
secret = random.randint(1,10)
guess = 0
tries = 0
while not guess == secret:
    guess = int(input("Please enter a number between 1-10: "))
    tries+=1
    if guess > secret:
        print("Too High")
        
    elif guess < secret:
        print("Too Low")
        #tries+=1
print("Success. ATTEMPTS TAKEN:", tries, "ATTEMPTS")