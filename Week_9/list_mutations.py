"""m_L = []
m_L.append(2)
m_L.append('a')
m_L.append(4)
m_L.append([1,2])

print(len(m_L))
print(m_L[0])
print(m_L[3])

m_L2 = [2,'a'] + [5,6]
print(m_L2)

print(max([3,5,0]))

m_L[3] = "The list is mutable!"
print(m_L)"""

"""m_list = ['a','b','c']
print("".join(m_list))

print("_".join(m_list))"""

"""m_list = [1,2,3]
print("".join(m_list))"""

"""great_name = "Hello Name"
great_name = great_name.split()
print(great_name)
great_name = "".join(great_name)
print(great_name)"""

"""def reverse_words(sentence):
    sentence = sentence.split()
    sentence = sentence[::-1]
    sentence = " ".join(sentence)
    return sentence

print(reverse_words("This is test"))"""

"""m_list1 = [4,2,7]

m_list1.sort()
print(m_list1)

m_list1.reverse()
print(m_list1)

m_list2 = sorted(m_list1)
print(m_list2)"""

"""def organize_words(sentence):
    sentence_seperated = sentence.lower().split()
    alphabetical_order = sorted(sentence_seperated)

    reverse_alphabetical = list(alphabetical_order)
    reverse_alphabetical.reverse() 
    
    sentence_reversed = list(sentence_seperated)
    sentence_reversed.reverse()

    return (alphabetical_order,reverse_alphabetical, sentence_reversed)

print(organize_words("This is a test"))"""
