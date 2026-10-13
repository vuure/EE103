import secret_number

number = secret_number.m_secretnum
guessed = False

guess = int(input("Guess the number: "))

"""

First Iteration

if(guess-number > 0):
    print("Guess is too high")
elif(guess-number < 0):
    print("Guess is too low")
elif(guess - number == 0):
    print("Guess is correct")
else:
    print("-1")

"""

"""

Second Iteration

while not guessed:
    guess = int(input("Guess the number: "))

    if(guess-number > 0):
        print("Guess is too high. Try Again")
    elif(guess-number < 0):
        print("Guess is too low. Try Again")
    elif(guess - number == 0):
        print("Guess is correct")
        guessed = True
    else:
        print("-1")

"""

"""

Third Iteration

for i in range(5):
    guess = int(input("Guess the number: "))

    if(guess-number > 0):
        print("Guess is too high. Try Again")
    elif(guess-number < 0):
        print("Guess is too low. Try Again")
    elif(guess - number == 0):
        print("Guess is correct")
        break
    else:
        print("-1")

while True:
    print("oh! no...")
    
"""