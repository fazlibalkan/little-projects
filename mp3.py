import pygame
import tkinter as tkr

"""Creating Window"""
player = tkr.Tk()

player.title("Audio Player")
player.geometry("205x340")

"""Get Song"""
file = "Song.mp3"


"""Action Event"""
def Play():
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()

def ExitPlayer():
	pygame.mixer.music.stop()



"""Buttons"""
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button1.pack(fill="x")
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
button2.pack(fill="x")

"""Songs"""
label1 = tkr.LabelFrame(player, text= "Song Name")
label1.pack(fill="both", expand="yes")
content1 = tkr.Label(label1, text = file)
content1.pack()



"""Activation"""
player.mainloop()