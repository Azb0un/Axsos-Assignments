function removeBlanks(str){
    var strArr=str.split(' ');
    console.log(strArr.join(""));
}


removeBlanks("Hello World, Welcome to coding")

console.log("---------------------------");

function getDigits(str){
    let digitsOnly = "";
    for (let i=0; i<str.length; i++){
        if (!isNaN(str[i])){
            digitsOnly += str[i];
        }
    }
    console.log(digitsOnly);
}

getDigits("asd12321dfa")

console.log("---------------------------");

function acronyms(str){
    let words = str.split(" ");
    let acronyms="";
    for (let i=0; i<words.length;i++){
        acronyms += words[i][0].toUpperCase();
    }
    console.log(acronyms);
}
acronyms("I'am a full-stack student")

console.log("---------------------------");

function countNoSpaces(str){
    let strArr = str.split(" ");
    let strJoin = strArr.join("");
    console.log(strJoin.length)
}

countNoSpaces("I'am a Full-stack student in axsos academy");

console.log("---------------------------");

function removeShorterStrings (arr, minLength) {
    let longArr = [];
    for (let i=0; i<arr.length; i++){
        if (arr[i].length >= minLength){
            longArr.push(arr[i]);
        }
    }
    console.log(longArr);
}
removeShorterStrings(["Ali", "Sarah", "Adam", "Yahya"], 4);