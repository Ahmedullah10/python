num = int(input("Enter a number: "))

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10
    digits = digits - 1;
if total == original:
    print("It is a Disarium number")
else:
    print("It is not a Disarium number")