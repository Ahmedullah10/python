var choice = prompt("Hi.Welcome to area calcualtor.\n Please Select shape to calculate area:\n1.Rectangle\n2.Triangle\n3.Circle\n4.Parallelogram\n5");

if (choice =='1') {
    var l =  prompt("Entre the lenght of rectangle")
    var b = prompt("Entre the breath for rectangle")
    var result = Number(l) * Number(b)
    Alert("Area of rectangle is: " + result)}

if (choice =='2') {
    var h = prompt("Entre the height of triangle")
    var b = prompt("Entre the base of triangle")
    var result = Number(h) * Number(b) / 2
    Alert("Area of triangle is:" + result)
}

if (choice == '3'){
    var r = prompt ("Entre the radius of circle")
    var result = 3.14 * Number(r) * Number(r)
    Alert("Area of circle is:" + result)
}

if (choice == '4'){
    var h = prompt ("Entre the height")
    var cb = prompt ("Entre the base ")
    var result = Number(h) * Number(cb)
    Alert("Area of parallelogram is:" + result)
}