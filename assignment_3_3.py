score = input("Enter Score:")
try:
    grade = float(score)
    if grade < 0 or grade > 1.0:
        print("error, enter 0 to 1.0")
except:
    exit()

if grade < 0.6 and grade >= 0:
    print("F")
elif grade < 0.7 and grade >= 0.6:
    print("D")
elif grade < 0.8 and grade >= 0.7:
    print("C")
elif grade < 0.9 and grade >= 0.8:
    print("B")
elif grade >= 0.9 and grade <= 1.0:
    print("A")
