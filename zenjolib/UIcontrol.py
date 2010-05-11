#!/usr/bin/python2.5
# -*- coding: utf-8 -*-

# ZenjoPlayer
# Copyright (C) 2009  
# Mateus Zenaide (matzenh@gmail.com) and Raniere Fernandes (raninho@raninho.com.br)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import os
from PyQt4 import QtCore, QtGui, uic

from zenjolib import constants
from zenjolib import audio
from zenjolib import tweet as twitter
from PyQt4.phonon import Phonon


app = QtGui.QApplication(sys.argv)
QtGui.QApplication.setApplicationName("ZenjoPlayer")
window = uic.loadUi(constants.uimain)
m_media = Phonon.MediaObject()
audioOutput = Phonon.AudioOutput(Phonon.MusicCategory)
Phonon.createPath(m_media, audioOutput)
playlist = []

m_media = Phonon.MediaObject()
audioOutput = Phonon.AudioOutput(Phonon.MusicCategory)
Phonon.createPath(m_media, audioOutput)

def play():
  indice = window.tbList.currentRow()
  if indice > -1:    
    window.lMusicName.setText("Ouvindo: " + playlist[indice][1] + " - " + playlist[indice][2])
    audio.play(playlist[indice][0],m_media)
  else:
    arquivo()

def next():
  indice = window.tbList.currentRow()
  if indice < (len(playlist)-1):
    window.tbList.setCurrentRow(indice+1)
  else:
    window.tbList.setCurrentRow(0)
  indice = window.tbList.currentRow()
  window.lMusicName.setText("Ouvindo: " + playlist[indice][1] + " - " + playlist[indice][2])
  audio.play(playlist[indice][0],m_media)

def tweet():
  indice = window.tbList.currentRow()
  if indice > -1:
    print("tweet")
    twitter.tweet("Ouvindo: " + playlist[indice][1] + " - " + playlist[indice][2])
  
def arquivo():
  musica = QtGui.QFileDialog.getOpenFileName(None,"Select Song", QtCore.QDir.homePath(), ("Musica (*.mp3)"))
  id3 = audio.getID3(musica)  
  addPlaylist(musica, id3[0], id3[1])   

def pasta():
  directory = QtGui.QFileDialog.getExistingDirectory()
  directory = directory.__str__()  
  for raiz, diretorios, arquivos in os.walk(directory):
    for arquivo in arquivos:
        if arquivo.endswith('.mp3'):
	  id3 = audio.getID3((directory + '/' +  arquivo))
	  addPlaylist((directory + '/' + arquivo), id3[0], id3[1])

def addPlaylist(path, artista, musica):
  newitem = QtGui.QListWidgetItem(artista + " - " + musica)
  window.tbList.addItem(newitem)  
  playlist.append([path.__str__(), artista, musica])

def main():
  
  window.show()  

  window.connect(window.BPlayPause, QtCore.SIGNAL("clicked()"), play)
  window.connect(window.BNext, QtCore.SIGNAL("clicked()"), next)
  window.connect(window.BTweet, QtCore.SIGNAL("clicked()"), tweet)

  window.connect(window.MArquivo, QtCore.SIGNAL("triggered()"), arquivo)
  window.connect(window.MPasta, QtCore.SIGNAL("triggered()"), pasta)
  window.connect(window.MSair, QtCore.SIGNAL("triggered()"), app.quit)
  window.connect(window.tbList, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), play)  

  sys.exit(app.exec_()) 
