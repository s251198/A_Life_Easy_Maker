def remember():
    ch=None
    while True:
        h=input("give or take:")
        if h=='give':
            x=input("enter your text and dont press enter until done:")
            ch=x
        elif h=='exit':
            break
        elif h=='take':
            print(ch)
        else:
            print("invalid input")
