let numbers = [1,2,2,3,4,4,5];
let newNumbers = [];
for(i=0; i<numbers.length; i++){

    let isDuplicate= false;

    for(x=0;x<newNumbers.length;x++){

        if(numbers[i]===newNumbers[x]){
            isDuplicate=true;
            break
        }
    }
    
    if(!isDuplicate){
        newNumbers.push(numbers[i])
    }
}
console.log(newNumbers);
