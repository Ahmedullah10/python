
var choice = prompt("Hi! Welcome to Perimeter Calculator.\nPlease select a shape:\n1. Rectangle\n2. Triangle\n3. Parallelogram");

if (choice == '1') {
    var l = prompt("Enter the length of rectangle");
    var b = prompt("Enter the breadth of rectangle");

    var result = 2 * (Number(l) + Number(b));

    alert("Perimeter of rectangle is: " + result);
}

if (choice == '2') {
    var a = prompt("Enter the first side of triangle");
    var b = prompt("Enter the second side of triangle");
    var c = prompt("Enter the third side of triangle");

    var result = Number(a) + Number(b) + Number(c);

    alert("Perimeter of triangle is: " + result);
}

if (choice == '3') {
    var s = prompt("Enter the side length of parallelogram");
    var b = prompt("Enter the base of parallelogram");

    var result = 2 * (Number(s) + Number(b));

    alert("Perimeter of parallelogram is: " + result);
}
