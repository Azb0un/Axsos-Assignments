function removeBlanks(str) {
    let newStr = "";
    for (let i = 0; i < str.length; i++) {
        if (str[i] != " ") {
            newStr += str[i];
        }
    }
    console.log(newStr);
}
removeBlanks("Hello World, Welcome to coding");

console.log("----------------------------------------");

function getDigits(str){
    var newStr = "";
    for(let i = 0 ; i < str.length ; i++ ){
        if((str[i] >= 0 || str[i] < 0)&& str[i]!==" "){
            newStr += str[i];
        }
    }
    console.log(newStr);
}
getDigits("I am 27 years old")

console.log("------------------------------------------");

function countNoSpace(str){
    let newStr="";
    for(i=0; i<str.length; i++){
        if (str[i]!==" "){
            newStr += str[i]
        }
    }
    console.log(newStr.length);
}
countNoSpace("I'am a Full-stack student in axsos academy");

console.log("------------------------------------------");

function acronyms (str){
    let newStr =str[0]+"";
    for(i=1; i<str.length; i++){
        if(str[i] == " "){
            newStr += str[i+1].toUpperCase()
        }
    }
    console.log(newStr);
}

acronyms("I'am a full-stack student")
