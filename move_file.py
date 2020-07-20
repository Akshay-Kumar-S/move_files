import os
import shutil
src = "/Users/akshaykumar/Desktop/photos/wed"
dirs = os.listdir(src)
f = open("wed.txt", "a")
for file in dirs:
	f.write(file+"\n")
	print(file)