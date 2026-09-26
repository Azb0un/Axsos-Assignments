for (let i=1; i <= 20; i++) {
    if (i % 2 === 1) {
        console.log(i);
    }
}

console.log("----------------");

for(let i=100; i>=0; i--){
    if (i % 3 === 0){
        console.log(i);
    }
}

console.log("----------------");

for (let i=4; i>= -3.5; i -= 1.5){
    console.log(i);
}

console.log("----------------");

let sum = 0;
for (let i=0; i<=100; i++){
    sum += i
}
console.log(sum);

console.log("----------------");

let factorial = 1;
for(let i=1; i<=12; i++){
    factorial *= i
}
console.log(factorial);
