#!/usr/bin/env python

# ANoise GUI 0.0.4 - http://launchpad.net/anoise
# Copyright (C) 2012-2015 Marcos Alvarez Costales https://launchpad.net/~costales
#
# ANoise is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# ANoise is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with ANoise; if not, see http://www.gnu.org/licenses 
# for more information.


import os, sys, glob, DistUtilsExtra.auto

# Create data files
data = [('/usr/share/anoise', glob.glob('anoise/*'))]

# Setup stage
DistUtilsExtra.auto.setup(
    name         = "anoise-gui",
    version      = "0.0.4",
    description  = "Ambient Noise GUI",
    author       = "Marcos Alvarez Costales https://launchpad.net/~costales",
    author_email = "https://launchpad.net/~costales",
    url          = "https://launchpad.net/anoise",
    license      = "GPL3",
    data_files   = data
    )

