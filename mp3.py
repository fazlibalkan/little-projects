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

def ExitPlayer():
	pygame.mixer.music.stop()



"""Buttons"""
button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)

"""Songs"""
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable = var)



"""Place Widgets"""
button1.pack(fill="x")
button2.pack(fill="x")
songtitle.pack()
playlist.pack(fill="both", expand= "yes")


"""Activation"""
player.mainloop()

