function longestCommonPrefix(arr){
    let prefix = "";
    let firstWord=arr[0];
    for(let i=0;i<firstWord.length;i++){
        let currentChar = firstWord[i]
        for(let x=1;x<arr.length;x++){
            if(arr[x][i] !== currentChar){
                return prefix;
            }
        }
        prefix+=currentChar
    }
    return prefix;
}
console.log(longestCommonPrefix(["flower","flight","flow"]))