unit conversion
def CelsiusFahrenheit():
    choice =int(input("enter the choice (1 or 2):"))
    temp=float(input("enter the temperature:"))
    if(choice==1):
        celsius=(temp*9/5)+32
        print("celsius:",celsius)
    elif(choice==2):
        fahrenheit=(temp-32)*5/9
        print("fahrenheit:",fahrenheit)
    else:
        print(exit)
        
def distancemiles():
    choice =int(input("enter the choice (1 or 2):"))
    temp=float(input("enter the distance:"))
    if(choice==1):
        miles=temp*0.621371
        print("miles:",miles)
    elif(choice==2):
        Km=temp//0.621371
        print("Kilometer:",Km)
    else:
        print(exit)
while True:
    print("\n=== Unit Converter ===")
    print("1. Temperature Conversion")
    print("2. Distance Conversion (km↔miles)")
    print("3. Exit")
    option=int(input("enter the option:"))
    if(option==1):
        CelsiusFahrenheit()
    elif(option==2):
        distancemiles()
    elif option == 3:
        print("exciting")
        break
    else:
        print("Invalid choice")
        
