hrs = input("Enter Hours:")
rate = input("Enter Rate")
h = float(hrs)
r = float(rate)
if h <= 40:
     gross_pay =  h * r
     print(float(gross_pay))
elif h > 40:
     gross_pay = (40 * r) + ((h-40) * (1.5*r))
     print(float(gross_pay))
