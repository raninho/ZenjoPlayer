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

from constants import body

if body == 'n8x0':
  from easy import audio
else:    
  from PyQt4.phonon import Phonon

def play(filename,m_media):
  m_media.setCurrentSource(Phonon.MediaSource(filename))
  m_media.play()

  

def getID3(filename):
  try:
    fp = open(filename, 'r')    
  except:
    print "ID3 - Erro"
  else:
    fp.seek(-128, 2)
    fp.read(3) # TAG iniziale
    title = fp.read(30)
    artist = fp.read(30)
    album = fp.read(30)
    anno = fp.read(4)
    comment = fp.read(28)
    fp.close()
    artist2 = artist.split("\x00")
    title2 = title.split("\x00")
    return [artist2[0],title2[0]]
 
