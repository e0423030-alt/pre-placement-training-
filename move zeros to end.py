arr = [0, 1, 0, 3, 12]
result=[]
count=0
for x in arr:
    if(x!=0):
        result.append(x)
    else:
        count+=1
for i in range(count):
    result.append(0)
    
print(result)
