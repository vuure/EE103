m_number = 158

m_binary = ""

while m_number > 0:
    m_binary = str(m_number % 2) + m_binary
    m_number //= 2

print(m_binary)