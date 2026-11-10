def countEven(evenOrOdd_method, m_num):
    even_count = 0
    for i in range(m_num + 1):
        if evenOrOdd_method(i) == "Even":
            even_count += 1
    return even_count