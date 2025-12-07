#checking the palindrome using th e number
s=input("enter the number:")
arr=[int(x) for x in s]
for i in range(len(arr)-1,-1,-1):
    for j in range(0,len(arr)):
        if(arr[i]!=arr[j]):
            break
            print("it is not palindrome")
print("it is palindrome")

#checking palindrome using the letter
s=input("Enter the string:")
arr=list(s)
rev=arr[::-1]
if(arr==rev):
    print("palindrome")
else:
    print("not palindrome")
