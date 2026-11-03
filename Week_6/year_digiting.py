m_year = int(input("Enter A Year: "))

m_digitcount = 0
m_digitsum = 0
m_pseudoyear = m_year
m_binaryresult = ""

while m_pseudoyear > 0:
    m_digitcount +=1
    m_pseudoyear //= 10

for i in range(m_digitcount):
    m_digitsum += m_year % 10
    m_year //= 10

print(m_digitsum / m_digitcount)