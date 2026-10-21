function reverseString(str) {
    let revStr = "";
    
    for(i=str.length - 1;i>=0;i--){
        revStr += str[i]
    }
    return revStr;
}
console.log(reverseString("Alli"));
console.log(reverseString("What If We Try This"));

