"""
m_input = input("Enter a 2-digit number between 00 and 24: ")
m_number = int(m_input)
m_binary = ""
while m_number > 0:
    m_binary = str(m_number % 2) + m_binary
    m_number //= 2
print(m_binary)
"""


student_id = int(input("Enter your Student ID: "))
number_of_digits = 0

student_id_digitcount = student_id
while student_id_digitcount > 0:
    number_of_digits +=1
    student_id_digitcount //= 10
powerof_ten = int(number_of_digits/2)
first_iteration = 10 ** powerof_ten

iteration_counter = 0
guess = first_iteration
while guess ** 2 < student_id:
    guess +=1
    iteration_counter +=1

guess_onebefore = (guess - 1) ** 2
guess = guess ** 2

if abs(guess - student_id) > abs(guess_onebefore - student_id):
    print(f'Closest perfect square to your ID is {guess_onebefore}')
else:
    print(f'Closest perfect square to your ID is {guess}')


"""
student_id = input("Enter your Student ID: ")
sum = 0
digit_counter = 0

for digit in student_id:
    sum = sum + int(digit)
    digit_counter +=1

arithmetic_mean = int(sum / digit_counter)

for i in range(arithmetic_mean):
    print(student_id)"""