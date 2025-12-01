p=float(input("enter the number:"))
r=float(input("enter the number:"))
t=float(input("enter the number:"))

SI=(p*r*t)/100
A=p*(1+(r/100))**t
CI=A-p
print("simple interest:",SI)
print("compound interest:",CI)
