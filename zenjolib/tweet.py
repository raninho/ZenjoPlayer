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

import twitter
import constants

def tweet(texto):
  username = constants.twitterUser
  password = constants.twitterPwd
  try:
    api = twitter.Api(username, password)
    api.PostUpdate(texto)
  except:
    print "Tweet: Erro"
  else:
    print "Tweet: Ok"
  


  
