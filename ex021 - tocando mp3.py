#Toque um MP3
import pygame

clip = mp3play.load(r'/Users/eduardolara/Music/01.mp3')

clip.play()

#tocar por 30 segundos e parar
import time
time.sleep(min(5, clip.seconds()))
clip.stop()