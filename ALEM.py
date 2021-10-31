import y, help, toss, draw, subprocess, dt
import stdiomask
import datetime
import webbrowser
from win32com.client import Dispatch
import os
ch=None
def search():
    from googlesearch import search
    import webbrowser
    #to search, will ask search query at the time of execution
    query = input("search:")
    #iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        webbrowser.open("https://google.com/search?q=%s" % query)

print("          ----------------          ")
print("        /                  \        ")
print("       /                    \       ")
print("      /  ------      ------  \      ")
print("     /  ||||||||    ||||||||  \     ")
print("    |    ------      ------    |    ")
print("    |                          |    ")
print("    |    ------      ------    |    ")
print("    |   ||||||||    ||||||||   |    ")
print("    |    ------      ------    |    ")
print("    |                          |    ")
print("     \   ------      ------   /     ")
print("      \ ||||||||    |||||||| /      ")
print("       \ ------      ------ /       ")
print("        \                  /        ")
print("          ----------------          ")
name=input("your good name:")
password=stdiomask.getpass()
if password=='s251198':
    
    try:
        import datetime
        greetm='Good morning '+name
        greeta='Good afternoon '+name
        greete='Good evening '+name
        currentTime = datetime.datetime.now()
        currentTime.hour
        if currentTime.hour < 12:
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak(greetm)

        elif 12 <= currentTime.hour <18:
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak(greeta)

        else:
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak(greete)
    except:
        pass
    e = datetime.datetime.now()
    if e.day== 14 and e.month== 11:
        speak = Dispatch("SAPI.Spvoice")
        speak.Speak("happy birthday Soumyadeep")
    try:
        import bs4
        from bs4 import BeautifulSoup as soup
        from urllib.request import urlopen

        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()

        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        # Print news title, url and publish date
        for news in news_list:
            print(news.title.text)
            print("-"*60)
    except:
        print()
        pass
            
    while True:
        try:
            q=input("how can i help you:").lower()
            if 'hello' in q:
                hello='hello '+name
                print('hello',name)
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak(hello)
            elif 'calculate' in q:
                x=int(input("enter int:"))
                a=int(input("enter int:"))
                y.calculate(x,a)
            elif 'remember' in q:
                while True:
                    h=input("give or take or exit:")
                    if h=='give':
                        x=input("enter your text and dont press enter until done:")
                        ch=x
                    elif h=='give':
                        print(ch)
                    elif h=='exit':
                        break
                    elif h=='take':
                        print(ch)
                        speak = Dispatch("SAPI.Spvoice")
                        speak.Speak(ch)
                    else:
                        print("invalid input")
            elif 'help' in q:
                help.help()
            elif 'toss' in q:
                toss.toss()
            elif 'draw' in q:
                draw.draw()
            elif 'entrar' in q:
                webbrowser.open('https://entrar.in/', new=2)
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('opening entrar')
            
            elif 'shutdown' in q:
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('your system will shutdown in few seconds')
                os.system('shutdown -s')
            elif 'restart' in q:
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('your system will restart in few seconds')
                os.system('shutdown -r')

            elif 'name' in q:
                n=input("do you want to change your name?")
                if 'yes' in n:
                    name=input("enter new name")
                    newname='Ok i will call you '+name
                    speak = Dispatch("SAPI.Spvoice")
                    speak.Speak(newname)
            elif 'google' in q:
                search()
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('This is what i got.')
            elif 'music' in q or 'spotify' in q:
                subprocess.spotify()
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('opening spotify')
            elif 'time' in q or 'date' in q:
                dt.dtime()
            elif 'alarm' in q:
                def alarm(set_alarm_timer):
                    import time, datetime
                    while True:
                        time.sleep(1)
                        current_time = datetime.datetime.now()
                        now = current_time.strftime("%H:%M:%S")
                        date = current_time.strftime("%d/%m/%Y")
                        
                        if now == set_alarm_timer:
                            try:
                                print("Time to Wake up")
                                while True:
                                    from win32com.client import Dispatch 
                                    speak = Dispatch("SAPI.Spvoice") 
                                    speak.Speak('time to wake up')
                            except:
                                break
                try:
                    set_alarm_timer=input("Alarm:")
                except:
                    set_alarm_timer=input("Alarm")
                alarm(set_alarm_timer)

            elif 'news' in q:
                import bs4
                from bs4 import BeautifulSoup as soup
                from urllib.request import urlopen

                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()

                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                # Print news title, url and publish date
                for news in news_list:
                    print(news.title.text)
                    print("-"*60)
            elif 'temperature' in q or 'weather' in q:
                import requests
                from pprint import pprint
                def weather_data(query):
                        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=4fe8b6add345d2bae50f88e7c98a3ec0&units=metric');
                        return res.json();
                def print_weather(result,city):
                        print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
                        print("Wind speed: {} m/s".format(result['wind']['speed']))
                        print("Description: {}".format(result['weather'][0]['description']))
                        print("Weather: {}".format(result['weather'][0]['main']))
                def main():
                        speak = Dispatch("SAPI.Spvoice")
                        speak.Speak('enter city name')
                        city=input('Enter the city:')
                        
                        print()
                        try:
                          query='q='+city;
                          w_data=weather_data(query);
                          print_weather(w_data, city)
                          print()
                        except:
                          print('City name not found...')
                if __name__=='__main__':
                        main()
            
            elif 'qrcode' in q or 'qr code' in q:
                import qrcode
                z=input("enter the string you want to display:")
                image.qrcode.make(z)
                image.save('qrcode_image.png')
                from PIL import Image
                img = Image.open("qrcode_image.png")
                img.show()
                
            elif 'exit' in q or q=='break' or 'bye' in q:
                print("bye")
                break
            elif 'hello, alem'== q or 'hello,alem'== q or 'hello alem'== q:
                print("hello, sir")
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('hello, sir')
            else:
                print("pardon??")
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak('Pardon??')
        except:
            continue

else:
    print("Access Denied")
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak('Access Denied')

        
