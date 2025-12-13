x=input("Enter the string:")
fre={}
for s in x:
    if s in fre:
        fre[s]+=1
    else:
        fre[s]=1
print(fre)
