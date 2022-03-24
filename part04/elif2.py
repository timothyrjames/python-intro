grade = float(input("What was the score?"))

print("The grade is:")
if grade > 91:
    print("A")
elif grade > 90:
    print("A-")
elif grade > 88:
    print("B+")
elif grade > 81:
    print("B")
elif grade > 80:
    print("B-")
elif grade > 78:
    print("C+")
elif grade > 71:
    print("C")
elif grade > 70:
    print("C-")
elif grade > 68:
    print("D+")
elif grade > 61:
    print("D")
elif grade > 60:
    print("D-")
else:
    print("F")

