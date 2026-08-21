num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def addition(a,b):
    return a + b
    
def multiplication(a,b):
    return a * b

choice = int(input("Enter your choice(1 for addition and 2 for multiplication): "))

if choice ==1:
    print("Sum =", addition(num1, num2))
    
elif choice ==2:
    print("Sum =", multiplication(num1, num2))
    
else:
    print("Invalid choice")