s=input("Enter the numbers:")
arr=list(s)
vowels=0
for x in arr:
    if x=="a"or x=="e" or x=="i"or x=="o"or x=="u":
        vowels+=1
    else:
       continue
print("vowels:",vowels)

#using string
s=input("Enter the numbers:")
vowels=0
for x in s:
    if x.lower() in "aeiou":
        vowels+=1
    else:
       continue
print("vowels:",vowels)
