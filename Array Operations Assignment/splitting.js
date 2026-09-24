
let iteams = ["a", "b", "c", "d", "e"];
let arrayA = [];
let arrayB = [];
for(i=0; i<iteams.length;i++){
    if (i<3){
        arrayA.push(iteams[i])
    }else {
        arrayB.push(iteams[i])
    }
}
console.log(arrayA);
console.log(arrayB);

