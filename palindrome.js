function palindrome(myString){
    var input = myString.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
    var reversed = input.split('').reversed().join('');

    if(input === reversedInput){
        document.write("<div>"+myString+" is a palindrome</div>");
    }  else {
        document.write("<div>"+myString+" is not a palindrome</div>");
    }
}

palindrome("madam")