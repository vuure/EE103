m_tuple = (10,20,(30,40),50,60)

print(len(m_tuple))
print(m_tuple[2][1])
print(m_tuple[-3][-1])

a = m_tuple[0]
b = m_tuple[1]

(a,b) = (b,a)
print(a,b)


def analyze_numbers(L):
    m_resultTuple = ()
    m_resultList = []
    total = 0
    for i in L:
        m_resultTuple += (i,)
        m_resultList.append(i**2)
        total += i
    return m_resultTuple, total, m_resultList

print(analyze_numbers([5,10,20,50]))


