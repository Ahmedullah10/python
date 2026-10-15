file = open("class-notes.txt", "w")
file.write("Complete Python homework\n")
file.write("Revise file handling concepts\n")
file.close()

print("File created successfully!")

file = open("class-notes.txt", "r")
print("\nFile contents:")
print(file.read())
file.close()

file = open("class-notes.txt", "a")
file.write("Practise Python programs\n")
file.close()

print("New information added!")

file = open("class-notes.txt", "r")

print("\nUpdated file contents:")
for line in file:
    print(line.strip())

file.close()
