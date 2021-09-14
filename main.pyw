# import all of tkinter
from tkinter import *

#This 4 import for just for logo. You can change logo with changing img_url variable
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

#import webbrowser
import webbrowser


#create a tkinter window
root = Tk()             

#open a window. Size 198x190
root.geometry('198x190')


#If you don't want to type webbrowser.open you can type it with a variable
wo = webbrowser.open


#Functions for commands
def google():
   wo("https://google.com")
def gmail():
   wo('https://gmail.com')
def github():
   wo('https://github.com')
def stackoverflow():
   wo('https://stackoverflow.com')
def twitter():
   wo('https://twitter.com')
def instagram():
   wo('https://instagram.com')
def youtube():
   wo('https://youtube.com')
def reddit():
   wo('https://reddit.com')
  
  
  
#Create a Button
btn1 = Button(root, text = 'Google', background='#5ead57', bd = '5', height = 1, width = 11, command = google)
btn2 = Button(root, text = 'Gmail', background='#fc2145', bd = '5', height = 1, width = 11, command = gmail)
btn3 = Button(root, text = 'Github', background='#b5b5b5', bd = '5', height = 1, width = 11, command = github)
btn4 = Button(root, text = 'Stack Overflow', background='#f2b53a', bd = '5', height = 1, width = 11, command = stackoverflow)                                               
btn5 = Button(root, text = 'Twitter', background='#46b9db', bd = '5', height = 1, width = 11, command = twitter) 
btn6 = Button(root, text = 'Instagram', background='#ff7ae0', bd = '5', height = 1, width = 11, command = instagram) 
btn7 = Button(root, text = 'YouTube', background='#ff0011', bd = '5', height = 1, width = 11, command = youtube) 
btn8 = Button(root, text = 'Reddit', background='#d4a644', bd = '5', height = 1, width = 11, command = reddit) 
btn9 = Button(root, text = 'Exit', background='#f20a40', bd = '5', height = 1, width = 11, command = root.destroy) 


#Set button position  
btn1.place(x=3, y=3)
btn2.place(x=3, y=42)  
btn3.place(x=3, y=82)
btn4.place(x=3, y=122)
btn5.place(x=102, y=3)
btn6.place(x=102, y=42)
btn7.place(x=102, y=82)
btn8.place(x=102, y=122)
btn9.pack(side = 'bottom')


# Next 5 line for application icon
img_url = "https://i.hizliresim.com/3nvaqsz.png" # Paste your image url between ""
response = requests.get(img_url)
img_data = response.content
p1 = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
root.iconphoto(False, p1)
root.configure(background = '#434a59') # Background color
root.title('Sites') # Application Title
root.mainloop()


