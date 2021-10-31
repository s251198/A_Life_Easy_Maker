#This program takes the date and time from the system and then prints the date and time.asctime
import datetime
def dtime():
    e = datetime.datetime.now() #For a much more clean code we are initiating this big code to one letter.
    print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year)) #The '%' in the middle gives the respective value to the '%s'

    print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
