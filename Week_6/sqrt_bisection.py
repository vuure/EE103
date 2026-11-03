import secret_data

m_number = secret_data.secret_number

m_lowerbound = 0
m_upperbound = m_number // 2

m_guess = (m_lowerbound + m_upperbound) // 2
m_guesscount = 0

while abs(m_guess**2 - m_number) > 0.00001:
    if m_guess**2 < m_number:
        m_lowerbound = m_guess+1
    else:
        m_upperbound = m_guess -1

    m_guess = (m_lowerbound + m_upperbound) / 2

    m_guesscount += 1

    if m_guesscount % 10 == 0:
        print("Current guess:", m_guesscount, m_guess)


print("The square root of", m_number, "is approximately", round(m_guess, 5))
print(m_guesscount, "times of guessing")