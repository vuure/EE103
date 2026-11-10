#Guess and Check algorithm

def guess_and_check(target):
    guess = 0
    num_guesses = 0

    while not guess**2 >= target :
        guess += 0.1
        num_guesses += 1

        if num_guesses % 1000 == 0:
            print("Current guess:", num_guesses, guess)

    print("The secret number is:", guess)
    print("Number of guesses:", num_guesses)

#Approximation algorithm

def approximate(target, epsilon, increment):
    guess = 0.0
    num_guesses = 0

    while abs(guess**2 - target) >= epsilon and guess <= target:
        guess += increment
        num_guesses += 1

        if num_guesses % 1000 == 0:
            print("Current guess:", num_guesses, guess)

    if abs(guess**2 - target) >= epsilon:
        print("Failed to find a close enough approximation.")
    else:
        print("The approximate square root is:", guess)
        print("Number of guesses:", num_guesses)

#Bisection search algorithm

def bisection_search(target, epsilon):
    low = 0
    high = target
    guess = (high + low) / 2.0
    num_guesses = 0

    while abs(guess**2 - target) >= epsilon:
        if guess**2 < target:
            low = guess
        else:
            high = guess

        guess = (high + low) / 2.0
        num_guesses += 1
        if num_guesses % 10 == 0:
            print("Current guess:", num_guesses, guess)

    print("The approximate square root is:", guess)
    print("Number of guesses:", num_guesses)