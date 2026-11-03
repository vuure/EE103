from secret_data import secret_year

m_guesshigh = 2026
m_guesslow = 0

m_guess = (m_guesslow + m_guesshigh) // 2

m_guesscount = 0

while m_guess != secret_year:
    if m_guess < secret_year:
        m_guesslow = m_guess + 1
    else:
        m_guesshigh = m_guess - 1
    m_guess = (m_guesslow + m_guesshigh) // 2

    m_guesscount += 1
    
print("The secret year is: ", m_guess)
print(m_guesscount, "times of guessing")