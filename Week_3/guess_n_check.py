m_squared_number = int(input("Write number to calculate its root: "))
guessed = False
start_index = 0

if m_squared_number < 0:
    print("Your number is negative. It has no root.")
    guessed = True

while not guessed:
    if start_index **2 == m_squared_number:
        print(f'The root is {start_index}')
        guessed = True
    elif start_index **2 > m_squared_number:
        print(f'Your number is not perfect square. Your root is between {start_index-1} and {start_index}')
        guessed = True

    start_index +=1