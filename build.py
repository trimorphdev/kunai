# build.py
#
# Builds a Kunai executable.
import os
from os import path

import glob
import sys

pathSeperator = '/'
if sys.platform.startswith('win32'):
  pathSeperator = "\\"

if path.exists("bin") == False:
  os.mkdir("bin")

files = glob.glob('**/*.cpp')
oFiles = []

for file in files:
  oFile = 'bin/' + (file[0:file.rindex('.')] + '.o').split(pathSeperator).pop()
  oFiles.append(oFile)
  cmd = "g++ -I include -std=c++11 -c " + file.replace('\\', '/') + " -o " + oFile
  print(" $ " + cmd)
  os.system(cmd)

print(" $ g++ " + " ".join(oFiles) + " -o bin/kunai")
os.system("g++ " + " ".join(oFiles) + " -o bin/kunai")

for file in oFiles:
  os.remove(file)