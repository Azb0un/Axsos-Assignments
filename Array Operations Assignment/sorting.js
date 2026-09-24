/*scores.sort((a, b) => a-b);
console.log(scores);

scores.sort((a, b) => b-a);
console.log(scores);
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"]
console.log(names.sort());
console.log(names);*/




let names=["Shatha","Sara", "Lina", "Sami", "Dalia"]

let scores = [50, 20, 70, 10, 40];
for (let i=0; i< scores.length; i++){
    for(let x=0 ; x < scores.length-i-1; x++){
        if(scores[x] > scores[x+1]){
            let temp= scores[x];
            scores[x]=scores[x+1];
            scores[x+1]= temp;
        }
    }
}
console.log(scores);


let numbers = [50,20,70,10,40];

for (let i=0 ; i<numbers.length; i++){
    for ( let x=0; x<numbers.length -i -1; x++){
        if(numbers[x] < numbers[x+1]){
            let temp=numbers[x];                
            numbers[x]=numbers[x+1];
            numbers[x+1]=temp;
        }
    }
} 
console.log(numbers);


console.log(names);
