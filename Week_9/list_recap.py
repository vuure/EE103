m_list = [5,10,15,20,[9,7],25]

m_list.append(30)
m_list.insert(2,12)
m_list.remove([9,7])
m_list[0] = 100
m_lastremoved = m_list.pop()

print(m_list)

m_list.sort()
list_ascending = list(m_list)
print(list_ascending)

m_list.sort(reverse = True)
list_descending = m_list
print(list_descending)

m_evenlist = [i for i in m_list if i%2==0]
print(m_evenlist)

m_oddsquarelist = [i**2 for i in m_list if not(i%2==0)]
print(m_oddsquarelist)

for i,v in enumerate(m_list):
    print(i,v)