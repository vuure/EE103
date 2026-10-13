m_number = int(input("Write number to calculate its factorial: "))

for i in range (m_number -1, 0, -1):
    m_number *= i

print(m_number)