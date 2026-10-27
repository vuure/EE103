m_squarednumber = int(input("Enter a number to find the square root of: "))

error_margin = 0.01

m_guess = 0
num_guesses = 0

m_increment = 0.0001

while not abs(m_squarednumber - m_guess**2) < error_margin and m_guess ** 2 < m_squarednumber:
    m_guess += m_increment
    num_guesses += 1

    if num_guesses % 1000 ==0:
        print("Current guess:", num_guesses, m_guess)

print("The square root of", m_squarednumber, "is approximately", m_guess)