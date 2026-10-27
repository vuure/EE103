m_start = int(input("Enter the starting number: "))
m_end = int(input("Enter the ending number: "))

result_for = 1

for i in range(m_start, m_end + 1):
    result_for *= i

print("The product of all numbers in the range is:", result_for)

result_while = 1
m_counter = m_end - m_start

while m_counter >= 0:
    result_while *= (m_start + m_counter)
    m_counter -= 1

print("The product of all numbers in the range using while loop is:", result_while)

if result_for == result_while:
    print("Both methods give the same result.")
else:
    print("The results from the two methods are different.")