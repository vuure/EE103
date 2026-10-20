m_number = 0.375

m_binary = "0."

while m_number > 0:
    m_number *= 2
    if m_number >= 1:
        m_binary += "1"
        m_number -= 1
    else:
        m_binary += "0"

print(m_binary)