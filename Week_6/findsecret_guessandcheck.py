from secret_data import secret_year

m_guess = 0

while m_guess != secret_year:
    m_guess += 1

print("The secret year is: ", m_guess)
print(m_guess, "times of guessing")