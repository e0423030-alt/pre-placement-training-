#using the sorted funcion
a=input("Enter the string a:")
b=input("Enter the string b:")
if(sorted(a)==sorted(b)):
    print("Anagram")
else:
    print("is not Anagram")

#using the dictionary 
a=input("Enter the a:")
b=input("Enter the b:")
if(len(a)!=len(b)):
    print("Is not Anagram")
else:
    frq1={}
    frq2={}
    
for x in a:
    frq1[x]=frq1.get(x,0)+1
    
for y in a:
    frq2[y]=frq2.get(y,0)+1
    
if(frq1==frq2):
    print("Anagram")
else:
    print("Is not Anagram")
    
