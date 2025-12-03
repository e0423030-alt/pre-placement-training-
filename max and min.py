#maximum
max=float('-inf')
arr=[89,34,56,78,80]
for i in range(len(arr)):
    if(arr[i]>max):
        max=arr[i]
print(max)

#minimum
min=float('inf')
arr=[89,34,5,56,7,78]
for i in range(len(arr)):
    if(arr[i]<min):
        min=arr[i]
print(min)
