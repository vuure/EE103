m_cubed_number = int(input("Write number to calculate its cube root: "))

guessed = False
isNegative = False
start_index = 0

if m_cubed_number < 0:
    isNegative = True

    m_cubed_number = abs(m_cubed_number)

while not guessed:
    if start_index **3 == m_cubed_number:
        print(f'The cube root is {(lambda x: -x if isNegative else x)(start_index)}')
        guessed = True
    elif start_index **3 > m_cubed_number:
        print(f'Your number is not a perfect cube. Your cube root is between {(lambda x: -x if isNegative else x)(start_index-1)} and {(lambda x: -x if isNegative else x)(start_index)}')
        guessed = True
        
    start_index +=1