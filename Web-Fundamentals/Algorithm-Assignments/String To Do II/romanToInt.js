function romanToInt (roman){
    const values = {I:1 , V:5, X:10, L: 50, C: 100, D: 500, M: 1000};
    let result = 0;
    for (let i = 0; i < roman.length; i++) {
        let current = values[roman[i]];
        let next = values[roman[i + 1]];
        if (next && current < next) { // checks if there is next first then check if current is smaller than it
            result = result - current; // in our example there is next so it will go through this line first wich will be -1
        } else {
            result = result + current; // the V has no next so we use this line and it will be 5
        }
    }
    return result; // since it start at -1 then 5 the result will be 4
}

console.log(romanToInt("IV"));
