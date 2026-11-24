m_list = [2,'a',4,[1,2]]

"""print(m_list)

print(len(m_list))
print(m_list[0])
print(m_list[-1])
print(m_list[3][0])
print(m_list[1:3])
print(m_list[-2::-1])"""

"""L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2

L3.append(L4)
L1.append(L3)

L = L1
print(L)"""

"""notes = ['do','re','mi']
notes.extend(['fa','so','la','si'])
notes.insert(6,'ti')
notes[0] = 'DO'
notes[1:3] = ['RE','Mİ']
notes.remove('ti')
last_note = notes.pop()
notes.pop(2)
del notes[0]
notes.reverse()
notes.sort()
notes.clear()"""

"""total = 0
dummy_range = range(10)

dummy_list_1 = []
for i in dummy_range:
    dummy_list_1.append(i)

dummy_list_2 = []
for i in range(10):
    dummy_list_2.append(i)

print(dummy_list_2)
print(dummy_list_1)

for i in dummy_list_1:
    total += i

print(total)"""

"""dummy_list = [x**2 for x in range(10)]
print(dummy_list)

for index, value in enumerate(dummy_list):
    print(index,value)"""

"""def lenght_and_square(m_list):
    m_lenght = len(m_list)
    for i,n in enumerate(m_list):
        m_list[i] = n**2

    return (m_lenght, m_list)

print(lenght_and_square([1,3,5]))"""

nums1 = [1,2]
nums2 = [2,3]

for i in nums1:
    for j in nums2:
        if j == i:
            break
        nums2.append(i)
        

print(nums2)
total = 0
for i,n in enumerate(nums2):
    total += n

average = total / len(nums2)

print(average)