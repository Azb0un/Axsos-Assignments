function removeEvenStrings (arr) {
    for (let i= arr.length-1; i>=0 ; i--){
        if (arr[i].length %2 === 0){
            arr.splice(i , 1);
        }
    }
    console.log(arr);
}
removeEvenStrings(["nope!", "its", "kris", "starting", "with", "k!", "(instead", "of", "Chris", "with", "C)", "."]);
