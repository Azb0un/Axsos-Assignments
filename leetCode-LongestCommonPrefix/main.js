
function longestCommonPrefix(arr) {
    if(arr.length === 0) return "";

    let prefix = "";
    const firstWord = arr[0];

    for(let x=0; x<firstWord.length; x++){
        const currentChar = firstWord[x];
        for(let i=1; i<arr.length; i++){
            if(arr[i][x] !== currentChar){
                return prefix;
            }
        }
        prefix = prefix + currentChar
    }
    return prefix;
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
