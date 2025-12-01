num=int(input("Enter the number:"))
binary=""
if(num==0):
    binary="0"
else:
    while(num>0):
        binary=str(num%2)+binary
        num=num//2
print("binary:",binary)

using the predefined method to find the binary
num=int(input("Enter the number:"))
print("binary:",bin(num)[2:])
