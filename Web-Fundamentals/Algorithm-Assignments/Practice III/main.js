function welcome() {
    console.log("Welcome to coding!");
}
welcome();

console.log("-----------------");

function square(n) {
    console.log(n ** 2);
}
square(3);

console.log("-----------------");

function convertToCelsius(f){
    return  (f - 32) * 5 / 9;  
}
console.log(convertToCelsius(105));

console.log("-----------------");

function isEven(number) {
    return number %2===0;
}
console.log(isEven(4));
console.log(isEven(5));

