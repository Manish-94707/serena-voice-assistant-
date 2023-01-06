import pyttsx3
import wikipedia
import datetime
import os
import webbrowser
import speech_recognition as sr
import subprocess as sp
import pywhatkit
import smtplib
from tkinter import *
from PIL import ImageTk, Image
print("INITIALIZING Serena....")

master = "Manish Sir"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.8)
engine.setProperty('voice',voices[1].id)



paths = {
    'notepad': "C:\\Windows\\notepad.exe",
    'screenshot':"C:\\Users\\HP\\Desktop\\Myproject(official)\\output\\screenshottaker.exe",
    'imagetopdf':"C:\\Users\HP\\Desktop\\Myproject(official)\\output\\imtopd.exe",
    'text to hand writing':"C:\\Users\\HP\\Desktop\\Myproject(official)\\output\\txttohand.exe",
    'audiobook':"C:\\Users\\HP\\Desktop\\Myproject(official)\\output\\AudioBook.exe",
    'voice calculator':"C:\\Users\\HP\\Desktop\\Myproject(official)\\output\\scicalcu.exe",
    'game':"C:\\Users\\HP\\Desktop\\Myproject(official)\\output\\game.exe",
    'music':"C:\\Users\\HP\\Desktop\\Myproject(official)\\Musicplayer.py",
    'trans' : "C:\\Users\\HP\\Desktop\\others\Myproject(official)\\python-language-translator.exe"   
}

def open_notepad():
    os.startfile(paths['notepad'])


def speak(text):
    engine.say(text)
    engine.runAndWait()



def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def wishme(): 
    hour=int(datetime.datetime.now().hour)
    
    
    if hour>=0 and hour<12:
        speak("Good morning" +master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +master)
    else:
        speak("Good Evening" +master)        

def takecommmand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio=r.listen(source)

    try:
        print("Recognizing......") 
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        query= None
    return query



class Widget:
    def __init__(self):
       root = Tk()
       root.title('manish')
       root.config(background='purple')
       root.geometry('720x480')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"D:\man1.jpeg"))
       panel = Label(root, image = img)
       panel.pack(side='right', fill='both',expand = "no")

       

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Run Serena\' to Give commands')

       userFrame = LabelFrame(root, text="User", font=('Black ops one',10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#FF7F24', fg='white')
       left2.config(font=("Times New Roman", 18, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Serena", font=('Black ops one',10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#1E90FF',fg='white')
       left1.config(font=("Times New Roman", 18, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Run Serena', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')
      
       
       
       self.compText.set('Hello, I am Serena! What can I do for you Sir ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()

    def clicked(self):
        print('Working')
        query = takecommmand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'wikipedia'in query:
            speak("Searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query.lower():
            speak("opening facebook")  
            webbrowser.open("facebook.com")  

        elif 'open instagram' in query.lower():
            speak("opening instagram")  
            webbrowser.open("instagram.com")

        elif 'open gmail' in query.lower():
            speak("opening g-mail")  
            webbrowser.open("gmail.com")

        elif 'open notepad' in query.lower():
            speak("opening notepad")
            os.startfile(paths['notepad'])
        
        elif 'snapshot' in query.lower():
            speak("opening screenshot")
            os.startfile(paths['screenshot'])

        elif 'open image to pdf' in query.lower():
            speak("opening imagetopdf")
            os.startfile(paths['imagetopdf'])
        
        elif 'translator' in query.lower():
            speak("your translator is ready")
            os.startfile(paths['trans'])

        elif 'open text to' in query.lower():
            speak("opening text to hand writing")
            os.startfile(paths['text to hand writing'])

        elif 'open audiobook' in query.lower():
            speak("opening audiobook")
            os.startfile(paths['audiobook'])

        elif 'bored' or 'play game' in query.lower():
            speak("let's have some fun")
            os.startfile(paths['game'])

        elif 'open music player' in query.lower():
            speak("opening music")
            os.startfile(paths['music'])

        elif 'open scientific calculator' in query.lower():
            speak("opening scientific calculator")
            os.startfile(paths['voice calculator'])

        elif 'open flipkart' in query.lower():
            speak("opening flipkart")  
            webbrowser.open("flipkart.com")

        elif 'play music' or 'play songs' in query.lower():
            speak("Alright sir playing music")
            songs_dir="D:\\music\\songs" 
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'play videos' in query.lower():
            speak("Alright here's some entertainment for you sir")
            video_dir="D:\\video"
            videos=os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))

        elif 'thank you' in query.lower():
            speak("sir no need to worry i am here for you")


        elif 'sorry' in query.lower():
            speak("well if you really are then say it to my master")

        elif' favourite game' in query.lower():
            speak("sir my favourite game is colour game if you wants to play then just say play game")

        elif 'please' in query.lower():
            speak("Don't say please sir!!!... I'm always here to help you")  

        elif 'How are you' in query.lower():
            speak("I am always good what about you sir?")    
                
        elif 'what can you do' in query.lower():
            speak("its better if you ask what kind of assistant you are")

        elif'what kind of assistant are you' in query.lower():
            speak("kind of helpful")

        elif'help me'in query.lower():
            speak("always ready to help you saksham sir")

        elif 'what is your name' in query.lower():
            speak("Serena sir")
            
        elif 'who made you' in query.lower():
            speak("manish sir")

        elif 'ok google' in query.lower():
            speak("thats not me sir....i am Serena")

        elif 'hey siri' in query.lower():
            speak("i am Serena sir,how can you forget something which is created by you sir") 

        elif 'i want to be rich' in query.lower():
            speak("so do i") 

        elif 'tell me joke ' in query.lower():
            speak("Sir i am not good in scarsam as you were")
    


if __name__ == '__main__':
    speak("INITIALIZING Serena")
    wishme()
    widget = Widget()  