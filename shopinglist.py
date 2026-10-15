file = open("shopping_list.txt", "w")

file.write("Milk\n")
file.write("Bread\n")
file.write("Eggs\n")
file.write("Apples\n")

file.close()

print("Shopping list created successfully!")


# PART 2: Read the complete file using read()
file = open("shopping_list.txt", "r")

print("\nComplete Shopping List:")
content = file.read()
print(content)

file.close()

file = open("shopping_list.txt", "a")

file.write("Rice\n")
file.write("Sugar\n")

file.close()

print("New items added successfully!")

file = open("shopping_list.txt", "r")

print("\nUpdated Shopping List:")

for line in file:
    print(line.strip())

file.close()

print("\nShopping list program completed!")
