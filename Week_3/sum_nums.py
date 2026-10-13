m_number = int(input("Write number to summing: "))

sum_gauss = ( m_number * (m_number + 1) ) / 2

for i in range(m_number -1,0,-1):
    m_number += i

if sum_gauss == m_number:
    print("Loop is correct")
else:
    print("Loop has a problem")