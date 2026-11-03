import secret_data

m_number = secret_data.secret_number

m_guess = 1
m_guesscount = 0

while not abs(m_number - m_guess**2) < 0.00001:
    m_guess = m_guess - ((m_guess ** 2 - m_number) / (2 * m_guess))
    m_guesscount += 1

print("The square root of", m_number, "is approximately", round(m_guess, 5))
print(m_guesscount, "times of guessing")