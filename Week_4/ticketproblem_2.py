total_ticket = 1000

for a in range(total_ticket+1):
    b = a - 20
    c = a * 2
    if b >= 0 and c >= 0 and a + b + c == total_ticket:
        print(f"Alyssa: {a}, Ben: {b}, Cindy: {c}")