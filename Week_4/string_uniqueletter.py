m_string = "testtesttest"

m_counter = 0

for number,letter in enumerate(m_string):
    for i in range(number,0,-1):
        if letter == m_string[i-1]:
            break
    else:
        print(letter)
        m_counter += 1

print(m_counter)