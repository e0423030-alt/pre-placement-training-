# using the string to remove the dupicates
x=input("enter the string:")
result=""
for ch in x:
    if ch not in result:
      result+=ch
print(result)

# using the arrya removing consecutive numbers
x = input("enter the string:")  
arr = [int(s) for s in x]

result = []
result.append(arr[0])  

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        result.append(arr[i])

print(result)
