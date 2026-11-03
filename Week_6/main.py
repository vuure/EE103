import say_hello
import triangle_area
import convertor

my_name = say_hello.say_my_name("test")

m_side = 5
m_area = triangle_area.calc_area(m_side)

m_convertednumber = convertor.binary_convertor(42)
print("The binary representation of", 42, "is:", m_convertednumber)
