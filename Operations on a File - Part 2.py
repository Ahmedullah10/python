import os

try:
    new_file = open('New_File.txt', 'x')
    new_file.close()
except FileExistsError:
    print("New_File.txt already exists.")

print("Checking whether my_file exists or not...")

if os.path.exists("my_file.txt"):
    print("File exists.")
else:
    print("File doesn't exist.")
    
    my_file = open("my_file.txt", "w")
    my_file.write("Hi, I am a penguin and I am 1 year old.")
    my_file.close()

if os.path.exists("Sample.txt"):
    os.remove("Sample.txt")
else:
    print("Sample.txt not found to remove.")

if os.path.exists("Folder") and os.path.isdir("Folder"):
    os.rmdir('Folder')
else:
    print("Folder directory not found to remove.")
