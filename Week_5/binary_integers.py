m_decimaltobinary = int(input("Enter a decimal number to convert to binary: "))

m_binarynumber = ""
while m_decimaltobinary > 0:
    m_remainder = m_decimaltobinary % 2
    m_binarynumber = str(m_remainder) + m_binarynumber
    m_decimaltobinary //= 2

print("The binary representation of the given number is:", m_binarynumber)