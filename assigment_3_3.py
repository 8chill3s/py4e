score = input("Enter Score:")
try:
    float(score)
    if score < 0 or score > 1.0:
except:
    print("error, your score is out of range")
    exit()
if score < 0.6 and score >= 0:
    print("F")
#elif score < 0.7 and score >= 0.6:
#    print("D")

elif score < 0.8 and score >= 0.7:
    print("C")

elif score < 0.9 and score >= 0.8:
    print("B")

elif score >= 0.9 and score <= 1.0:
    print("A")
