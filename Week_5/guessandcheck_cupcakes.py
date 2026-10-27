m_totalcupcakes = 28

for d in range(m_totalcupcakes + 1):
    for e in range(m_totalcupcakes + 1):
        for f in range(m_totalcupcakes + 1):
            if e - 3 == d and f/3 == d and e + f + d == m_totalcupcakes:
                print("The number of cupcakes David has is:", d)
                print("The number of cupcakes Emma has is:", e)
                print("The number of cupcakes Frank has is:", f)