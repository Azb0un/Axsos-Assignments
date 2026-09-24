function alwaysHungry(arr) {
    let foundFood = false;
    for(i=0;i<arr.length;i++){
        if (arr[i] === "food"){
            console.log("yummy");
            foundFood = true;
        } 
    }
    if (!foundFood){
        console.log("I'm hungry");
        
    }
}
alwaysHungry([ "pie", 3.14, "Alli", "food"])

console.log("-----------------");

function highPass(arr, cutoff){
    var filteredArr = [];
    for ( i=0; i<arr.length; i++){
        if (arr[i] > cutoff){
            filteredArr.push(arr[i])
        }
    }
    console.log(filteredArr);
}
highPass([6,2,4,8,1,5,9], 5);

console.log("-----------------");

function betterThanAvg (arr){
    var sum = 0;
    for(i=0; i<arr.length; i++){
        sum = sum + arr[i]
    }
    var average = sum/arr.length;
    var count = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i]>average) {
            count =count + 1;
        }
    }
        return count
}

console.log(betterThanAvg([1,2,3,4,5,6,7,8,9,10]));

console.log("-----------------");

function reverse(arr){
    let reverse=[];
    for (let i=arr.length - 1; i>=0 ; i--){
        reverse.push(arr[i]);
    }
    console.log(reverse);
}
reverse(["a","b","c","d","e","f"]);


console.log("-----------------");

function fibonacciArray (n){
    var fibArr = [0,1];
    for (i=2; i<n ; i++){
        var nextValue = fibArr[i-1]+fibArr[i-2];
        fibArr.push(nextValue);
    }
    return fibArr;
}

console.log(fibonacciArray(11));
//index 10 = index9 + index8