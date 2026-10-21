let numbers = [5, 10, 15, 20, 25];
/*if (numbers.includes(25)) {  
    console.log("Found at position"+" "+(numbers.indexOf(25)+1));
}else {
    console.log("Not found");
}*/

for (i=0; i<numbers.length; i++){
    if (numbers[i]==25){
        console.log("Found at position "+ (i+1));
        break; 
    }if(i == numbers.length -1) {
        console.log("not found");
    }
}
