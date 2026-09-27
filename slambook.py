import sys

def initial_slambook():

    rows, cols = int(input("Please enter initial number of friends: ")), 5

    slam_book = []
    print(slam_book)

    for i in range(rows):

        print("\nEnter friend %d details in the following order:" % (i + 1))
        print("NOTE: * indicates mandatory fields")
        print("........................................................")

        temp = []

        for j in range(cols):

            if j == 0:
                temp.append(str(input("Enter name*: ")))

                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field.")

            if j == 1:
                temp.append(int(input("Enter age*: ")))

            if j == 2:
                temp.append(str(input("Enter favorite color: ")))

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
         
            if j == 3:
                temp.append(str(input("Enter hobby: ")))

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter favorite food: ")))

                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        slam_book.append(temp)

    print("\nYour Slambook:")
    print(slam_book)

    return slam_book


def menu():

    print("\n****************************************")
    print("              MY SLAMBOOK")
    print("****************************************")

    print("1. Add a new friend")
    print("2. Remove a friend")
    print("3. Delete all friends")
    print("4. Search for a friend")
    print("5. Display all friends")
    print("6. Exit Slambook")

    choice = int(input("Please enter your choice: "))

    return choice


# Add a new friend
def add_friend(sb):

    friend = []

    friend.append(str(input("Enter name: ")))
    friend.append(int(input("Enter age: ")))
    friend.append(str(input("Enter favorite color: ")))
    friend.append(str(input("Enter hobby: ")))
    friend.append(str(input("Enter favorite food: ")))

    sb.append(friend)

    return sb


def remove_friend(sb):

    query = str(input("Enter the name of the friend you want to remove: "))

    for i in range(len(sb)):

        if query == sb[i][0]:

            print(sb.pop(i))
            print("Friend has been removed.")

            return sb

    print("Friend not found.")

    return sb


def delete_all(sb):

    sb.clear()

    return sb

def search_friend(sb):

    query = str(input("Enter the name of the friend you want to search: "))

    for i in range(len(sb)):

        if query == sb[i][0]:

            print("\nFriend found:")
            print(sb[i])

            return i

    return -1


# Display all friends
def display_all(sb):

    if not sb:

        print("Slambook is empty: []")

    else:

        for i in range(len(sb)):
            print(sb[i])

def thanks():

    print("\n****************************************")
    print("Thank you for using My Slambook!")
    print("Please visit again!")
    print("****************************************")

    sys.exit("Goodbye!")


print("........................................................")
print("Hello! Welcome to My Slambook")
print("You can now create and manage your Slambook.")
print("........................................................")


ch = 1

sb = initial_slambook()

while ch in (1, 2, 3, 4, 5):

    ch = menu()

    if ch == 1:
        sb = add_friend(sb)

    elif ch == 2:
        sb = remove_friend(sb)

    elif ch == 3:
        sb = delete_all(sb)

    elif ch == 4:

        d = search_friend(sb)

        if d == -1:
            print("Friend does not exist. Please try again.")

    elif ch == 5:
        display_all(sb)

    else:
        thanks()