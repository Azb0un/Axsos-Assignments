let array1 = [1,2,3];
let array2 = [4,5,6];
/*let array3 = [...array1 , ...array2]
console.log(array3);*/

let array3 = [];

for ( i=0; i<array1.length; i++){
    array3.push(array1[i])
}
for (i=0; i<array2.length; i++){
    array3.push(array2[i])
}
console.log(array3);
