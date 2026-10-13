m_number = int(input("Write number to calculate its factorial: "))
counter = m_number -1

while counter > 0:
    m_number *= counter
    counter -= 1

print(m_number)
