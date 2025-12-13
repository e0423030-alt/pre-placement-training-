a=[2,3,1,34,5]
b=[12,4,5,6,78,9]
i=0
j=0
a.sort()
b.sort()
result=[]
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1
        
while(i<len(a)):
        result.append(a[i])
        i+=1
while(j<len(b)):
        result.append(b[j])
        j+=1
print(result)
    
    
