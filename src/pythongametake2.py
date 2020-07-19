# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#!/usr/bin/python

import tkinter
import tkinter.font as tkfont
import os
from PIL import Image, ImageTk


top = tkinter.Tk()
# Code to add widgets will go here...
top.title("Hangman !!!")
top.geometry("900x300")
base_folder = os.path.dirname(__file__)
#image_paths = ['hangman.png']
image_path = os.path.join(base_folder, 'hangman.png')
hangmanimg = Image.open(image_path)
hangmanimg = ImageTk.PhotoImage(hangmanimg)
panel = tkinter.Label(top, image = hangmanimg).pack(side = "left")
panel2 = tkinter.Label(top,padx = 20,pady =  20,text = "Guess the word").pack(side = "top")
answer = "test"
wordEntry = tkinter.Entry(top)
wordEntry.pack(side = 'bottom')
fontStyle = tkfont.Font(family="Lucida Grande 18 bold", size=50)


#print(userGuess)

def display_letters(numberOfChances,wordDisplay):
    #print(wordEntry.get())
    #print("to be continued !!!")
   # while True:
   numberOfChances = 5
   wordDisplay = ''
   for i in answer:
     wordDisplay+='-'
    userGuess = wordEntry.get()
    #panel3.pack_forget()
    if len(wordEntry.get()) != 1:
        warning = tkinter.Tk()
        warning.title("Warning!!")
        numberOfChances -= 1
        print (numberOfChances)
        wpanel = tkinter.Label(warning, text = "Only enter one character at a time", font='Helvetica 18 bold').pack(side = 'left')
        
    if numberOfChances == 0:
        lose = tkinter.Tk()
        lose.title("You Lose !!!")
        lpanel = tkinter.Label(lose,text = "Well, you lost. Better luck next time !",font='Helvetica 18 bold').pack(side = 'left')
        top.destroy()
    if answer.find(userGuess):
            change_display(wordDisplay,userGuess)
    else:
        numberOfChances-=1
            
   # userGuess = ''.join(newUserGuess)
    #if wordEntry.get() not in userGuess:
   #     numberOfChances -=1
   # print (userGuess)
   # print (numberOfChances)
    
    
    

panel3 = tkinter.Label(top,text = wordDisplay,font = fontStyle)
panel3.pack(side = 'bottom')
               
button = tkinter.Button(top,text='SUBMIT',width = 30,command=lambda:display_letters(numberOfChances,wordDisplay))
button.pack(side = 'right')
def change_display(wordDisplay,userGuess):
    pos = 0
    #code for changing word displayed will be added here
    for i in range(0,len(answer)):
        if answer[i] == userGuess:
            pos = i
    wordDisplay = list(wordDisplay)
    wordDisplay[pos] = userGuess
    wordDisplay = "".join(wordDisplay)
    print(wordDisplay)
#panel3 = tkinter.Label(top,text = userGuess,font = fontStyle).pack(side = 'bottom')
top.mainloop()    

    