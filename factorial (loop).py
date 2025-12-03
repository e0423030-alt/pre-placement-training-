#factorial using loop

n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


#using the recursion
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
print(fact(5))
