#left pyramid
x=int(input("Enter the number:"))
for i in range(1,x+1):
    print("*" *i)

#invertible pyramid
x=int(input("Enter the number:"))
for i in range(x,0,-1):
    print("*" *i)

# right pyramid
x=int(input("Enter the number:"))
for i in range(1,x+1):
    print(" " * (x-i) + "*" * i)

#center pyramid
x=int(input("Enter the number:"))
for i in range(1,x+1):
    print(" " * (x-i) + "*" *(2*i-1))
  
#invertible pyramid
x=int(input("Enter the number:"))
for i in range(x,0,-1):
    print(" " * (x-i) + "*" *(2*i-1))

#diamond pyramid
x=int(input("Enter the number:"))
for i in range(1,x+1):
    print(" "*(x-i)+"*"*(2*i-1))
for j in range(x,0,-1):
    print(" "*(x-j)+"*"*(2*j-1))
