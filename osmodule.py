import os
from datetime import datetime
print(dir(os))
# os.chdir("/home/utku/Desktop")
print(os.getcwd())
print(os.listdir())
print(os.getcwd())
os.mkdir("Dir1")
os.makedirs("Dir2/Dir3")
os.rmdir("Dir2/Dir3")
os.mkdir("Dir2/Dir3")
os.rmdir("Dir1")
os.removedirs("Dir2/Dir3")
os.rename("test.txt", "test2.txt")
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))
print(os.walk("/home/utku/Desktop"))
for dir_path, dir_name, file_name in os.walk("/home/utku/Desktop"):
    print("Dir Path ", dir_path)
    print("Dir Name ", dir_name)
    print("File Name ", file_name)
    print("*******************************")
    for i in file_name:
        if i.endswith(".py"):
            print(i)

