# are you confused take a toss
from win32com.client import Dispatch
def toss():
    import random
    while True:
        ch = input("want to toss?").lower()
        x=random.randint(0,1)
        if ch == 'yes' or ch == 'y' or ch== 'Y':
            if x==1:
                print("heads")
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('heads')
            else:
                print("tails")
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('tails')
            continue
        else:
            print("thanks for playing")
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak('thanks for playing')
            break
    
