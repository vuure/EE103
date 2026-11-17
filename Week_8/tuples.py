m_tuple = (2,'a',4,(1,2))
"""print(m_tuple)

print(len(m_tuple))
print(m_tuple[0])
print(m_tuple[-1])
print(m_tuple[3][0])
print(m_tuple[1:3])
print(m_tuple[-2::-1])"""

#x = 1
#y= 2

"""temp = 0

temp = x
x = y
y = temp """

#(x,y) = (y,x)

#print(x,y)

"""m_fullname = "John Smith"

def name_splitter(fullName):
    fullName = fullName.split()
    return (fullName[0], fullName[1])

print(name_splitter(m_fullname))

def vowel_counter(fullName):
    fullName = fullName.lower()
    consonants = 0
    vowels = 0
    for letter in fullName:
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1
    return (vowels, consonants)

print(vowel_counter(m_fullname))"""

"""def mean_average (*args):
    total = 0
    for number in args:
        if type(number) == int or type(number) == float:
            total += number
    return total / len(args)

print(mean_average(1,2,3,4,5))"""

#print(type((1)))
#print(type((1,)))

