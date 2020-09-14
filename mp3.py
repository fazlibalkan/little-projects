import pygame
import tkinter as tkr
import os

"""Creating Window"""
player = tkr.Tk()

player.title("Audio Player")
player.geometry("205x340")

"""Playlist Register"""
os.chdir("D:/mp3-player/mp3-player/Songs")
print(os.getcwd)
songlist = os.listdir()


"""Volume"""
VolumeLevel = tkr.Scale(player, from_= 0.0, to_=1.0, orient = tkr.HORIZONTAL, resolution = 0.1)

"""Playlist"""
playlist = tkr.Listbox(player, highlightcolor = "blue", selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
	pos = 0
	playlist.insert(pos, item)
	pos = pos + 1


"""Pygame Inits"""
pygame.init()
pygame.mixer.init()


"""Action Event"""
def Play():
	pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
	var.set(playlist.get(tkr.ACTIVE))
	pygame.mixer.music.play()
	pygame.mixer.music.set_volume(VolumeLevel.get())

def ExitPlayer():
	pygame.mixer.music.stop()

def Pause():
	pygame.mixer.music.pause()

def Unpause():
	pygame.mixer.music.unpause()


"""Buttons"""
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=Unpause)



"""Songs"""
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)



"""Place Widgets"""
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
VolumeLevel.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand= "yes")


"""Activation"""
player.mainloop()

