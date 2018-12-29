#T is no of test method
#N is interger no

T=int(input("T:"))
if T<=1000:
    print(T)
else:
    print("input not grater than 1000")
for i in range(T):
    N=int(input("\nN:"))
    if N<=1000:
        print(N)
    else:
        print("N not greater than 1000")
    for j in range(N):
        print(j+1, end=' ')
        
    yb=int(input("\nyear:"))
    if yb>=1:
        mb=int(input("month:"))
        if mb<=12:
            db=int(input("date:"))
            if db>31:
                print("invilid input")
    
    print(yb,mb,db, end=' ')
    y=int(input("\nyear:"))
    if y>yb:
        m=int(input("month:"))
        if m<=12:
            d=int(input("date:"))
            if d>31:
                print("invilid input")
    elif y==yb:
        m=int(input("month:"))
        if m>mb:
            d=int(input("date:"))
            if d>31:
                print("invilid input")
        elif m==mb:
            if d>=db:
                d=int(input("date:"))
                if d>31:
                    print("invilid input")
    else:
        print("invilid input")
    print(y,m,d, end=' ')
    
if d< db:
    d += 30
    m -= 1
if m< mb:
    m += 12
    y -= 1
# These lines calculate years, months and days.  
age=((y-yb)*365)+((m-mb)*30)+(d-db)
print( "\n",age,"\n")