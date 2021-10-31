def calculate(x,y):
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    choice=input("choice:")

    if choice=='1':
        c=x+y
        print(c)

    elif choice=='2':
        c=x-y
        print(c)

    elif choice=='3':
        c=x*y
        print(c)

    elif choice=='4':
        c=x/y
        print(c)

    elif choice==' ':
        print("invalid input")

    elif choice==None:
        print("invalid input")

    else:
        print("invalid input")
