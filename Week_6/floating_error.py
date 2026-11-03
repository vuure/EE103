m_x = 0.1
m_y = 0.2

m_z = m_x + m_y

if(m_z == 0.3):
    print("Equal")
else:
    print("Not Equal")

if (abs(m_z - 0.3) < 1e-9):
    print("Equal")
else:
    print("Not Equal")