
max1=float('-inf')
max2=float('-inf')
s=input("Enter the number:")
arr=s.split(",")
arr=[int(x) for x in arr]
for u in arr:
    if(u>max1):
        max2=max1
        max1=u
    elif(u>max2 and u!=max1):
        max2=u
print("1st largest no:",max1)
print("2nd largest no:",max2)
