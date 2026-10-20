total_ticket = 10

for a in range(11):
    for b in range(11):
        for c in range(11):
            if a-2==b and a*2 == c and a+b+c == total_ticket:
                print(f"Alyssa: {a}, Ben: {b}, Cindy: {c}")
