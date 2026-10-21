function twoSum(arr, target){
    var storedValues={};// make empty object
    for (let i = 0; i < arr.length; i++) {
        var currentValue = arr[i]; 
        var neededValue = target - currentValue;
        if(neededValue in storedValues){
            return [storedValues[neededValue], i]
        }else {
            storedValues[currentValue] = i; //store in the object
        }
    }
}
console.log(twoSum([11, 13, 7, 2], 9));
console.log(twoSum([3,3], 6));
console.log(twoSum([1,5,9,8,2], 3));

