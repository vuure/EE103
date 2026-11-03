midterm = float(input("Enter midterm score: "))
final = float(input("Enter final score: "))

average = (midterm * 0.4) + (final * 0.6)

print(f"Average: {average:.2f}")

if average >= 80:
    print("Excellent!")
elif average >= 60:
    print("Passed")
else:
    print("Failed")
