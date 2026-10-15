
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

# PART 1: Write notes into a file
file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()

print("Class notes saved successfully!")

# PART 2: Display daily tasks
print("\nDo school homework")
print("\nDo Python homework")
print("\nPlay with friends")
print("\nDo dinner on time")
print("\nStudy")
print("\nSleep early")

