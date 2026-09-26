let i = -5
if (i>0) {
    console.log("positive");
}else if (i<0) {
    console.log("negative");
}
else{
    console.log("its zero");
}
console.log("-------------");

let time = 15;
if (time < 12) {
    console.log("Good morning");
}else {
    console.log("Good afternoon");
}
console.log("-------------");

let grade = 87;
if (grade >= 90) {
    console.log("A");
} else if (grade >=80) {
    console.log("B");
}else if (grade >= 70) {
    console.log("C");
}else{
    console.log("F");
}
console.log("-------------");

let day ="sunday";
switch (day) {
    case "saturday":
        console.log("weekend");
        break;
    case "sunday":
        console.log("weekend");
        break;
    default:
        console.log("weekday");
        break;
}