def leaper_check(year:int)->bool:
    return (year%4==0) and (year%100!=0 or year%400==0)
def main():
    try:
        y=int(input("enter the year:"))
    except ValueError:
        print("Please enter the valid year")
    if leaper_check(y):
        print(f"{y} is a leaper")
    else:
        print(f"{y} is not leaper")
        
if __name__=="__main__":
    main()
