from tkinter import *
from PIL import Image, ImageTk
from random import randint
import pygame

pygame.mixer.init()
pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play()

root = Tk()
root.title("RPS_Project")
root.configure(background="#DFFF9E")


rock_img =ImageTk.PhotoImage(Image.open("rock.png"))
paper_img =ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img =ImageTk.PhotoImage(Image.open("scissor.png"))
crock_img =ImageTk.PhotoImage(Image.open("crock.png"))
cpaper_img =ImageTk.PhotoImage(Image.open("cpaper.png"))
cscissor_img =ImageTk.PhotoImage(Image.open("cscissor.png"))
userlogo_img=ImageTk.PhotoImage(Image.open("user.png"))
cpulogo_img=ImageTk.PhotoImage(Image.open("cpu.png"))
game_logo_img=ImageTk.PhotoImage(Image.open("gamelogo.png"))

game_label=Label(root,image=game_logo_img,bg="#DFFF9E")#Game Img
userl=Label(root,image=userlogo_img,bg="#DFFF9E")#User logo Pic
c_label=Label(root,image=cpulogo_img,bg="#DFFF9E")#computer Logo pic
user_label=Label(root,image=paper_img,bg="#DFFF9E")
comp_label=Label(root,image=cpaper_img,bg="#DFFF9E")

game_label.grid(row=0,column=2)
userl.grid(row=1,column=1)
c_label.grid(row=1, column=3)
user_label.grid(row=5,column=1)
comp_label.grid(row=5,column=3)

user_score=Label(root,text=0,font="lucid 25",bg="#DFFF9E")
comp_score=Label(root,text=0,font="lucid 25",bg="#DFFF9E")
comp_score.grid(row=3,column=3)
user_score.grid(row=3,column=1)


user_indicator=Label(root, font=50, text="USER", bg="#DFFF9E", fg="#FF7F50")
comp_indicator=Label(root, font=50, text="COMPUTER", bg="#DFFF9E", fg="#FF7F50")

user_indicator.grid(row=2, column=1)
comp_indicator.grid(row=2, column=3)

#messages
msg=Label(root,font="lucid 20", bg="#DFFF9E", fg="#F54764")
msg.grid(row=5,column=2)

def updatemsg(x):
    msg['text']=x
    if x == "Its a TIE !!!":
        msg['fg']="#F6BE00"
    elif x== "~~~You Loose~~~":
        msg['fg']="red"
    else:
        msg['fg']="green"


def updateuserscore():
    uscore=int(user_score["text"])
    uscore+=1
    user_score["text"]=str(uscore)
    update_color(user_score["text"], comp_score["text"])
def updatecompscore():
    cscore = int(comp_score["text"])
    cscore += 1
    comp_score["text"] = str(cscore)
    update_color(user_score["text"], comp_score["text"])


def checkresult(player,computer):
    if player==computer:
        updatemsg("Its a TIE !!!")
    elif player=="rock":
        if computer=="paper":
            updatemsg("~~~You Loose~~~")
            updatecompscore()
        else:
            updatemsg("*** You Win ***")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemsg("~~~You Loose~~~")
            updatecompscore()
        else:
            updatemsg("*** You Win ***")
            updateuserscore()

    elif player=="scissor":
        if computer=="rock":
            updatemsg("~~~You Loose~~~")
            updatecompscore()
        else:
            updatemsg("*** You Win ***")
            updateuserscore()

    else:
        pass


def update_color(a,b):
    if(int(a)>int(b)):
        user_score['fg']="green"
        comp_score['fg']="red"
    elif(int(a)==int(b)):
        user_score['fg'] = "#F6BE00"
        comp_score['fg'] = "#F6BE00"
    else:
        user_score['fg'] = "red"
        comp_score['fg'] = "green"

#update choice

choices=["rock","paper","scissor"]


def updateChoice(x):
    compchoice = choices[randint(0,2)]
    if compchoice=="rock":
        comp_label.configure(image=crock_img)
    elif compchoice=="paper":
        comp_label.configure(image=cpaper_img)
    else:
        comp_label.configure(image=cscissor_img)


    checkresult(x,compchoice)
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

rock=Button(root,width=30,height=2,text="ROCK", command=lambda:updateChoice("rock"),bg="#FF4500",fg="white").grid(row=7,column=1)
paper=Button(root,width=30,height=2,text="PAPER",command=lambda:updateChoice("paper"),bg="#FAD02E",fg="white").grid(row=7,column=2)
scissor=Button(root,width=30,height=2,text="SCISSOR",command=lambda:updateChoice("scissor"),bg="#00BBFF",fg="white").grid(row=7,column=3)

admi=Label(root, font=50, text="-:By:-", bg="#DFFF9E", fg="#FF7F50")
admin_detail=Label(root, font=50, text="KULDEEP KUSHWAHA", bg="#DFFF9E", fg="#FF7F50")

admi.grid(row=8, column=2)
admin_detail.grid(row=9, column=2)

root.mainloop()
