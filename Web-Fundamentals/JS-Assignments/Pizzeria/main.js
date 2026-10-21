function pizzaOven(typeOfCrust,typeOfSauce,typeOfCheeses,pizzaToppings){
    var pizza = {};
    pizza.typeOfCrust = typeOfCrust;
    pizza.typeOfSauce = typeOfSauce;
    pizza.typeOfCheeses = typeOfCheeses
    pizza.pizzaToppings = pizzaToppings
    return pizza;
}

let p1=pizzaOven("deep dish","traditional",["mozzarella"], ["pepperoni", "sausage"]);
console.log(p1);
let p2=pizzaOven("hand tossed","marinara",["mozzarella", "feta"],["mushrooms", "onions", "olives"])
console.log(p2);
let p3=pizzaOven("neapolitan", "traditional",["mozzarella"],["basil"]);
console.log(p3);
let p4=pizzaOven("sicilian", "white sauce",["mozzarella"],["chicken","mushrooms"]);
console.log(p4);

function randomPizza(){
    const crusts = ["deep dish", "hand tossed", "neapolitan", "sicilian"];
    const sauces = ["traditional", "marinara", "white sauce", "pesto"];
    const cheeseOptions = ["mozzarella", "parmesan", "feta"];
    const toppingOptions = ["pepperoni", "sausage", "mushrooms", "olives", "onions", "chicken"];

const crust = crusts[Math.floor(Math.random()*crusts.length)];
const sauce = sauces[Math.floor(Math.random()*sauces.length)];

const numCheeses = Math.floor(Math.random() * 2) + 1;
const cheeses = [];
while (cheeses.length < numCheeses) {
    const cheese = cheeseOptions[Math.floor(Math.random() * cheeseOptions.length)];
    if (!cheeses.includes(cheese)) cheeses.push(cheese);
}

const numToppings = Math.floor(Math.random() * 2) + 2;
const toppings = [];
while (toppings.length < numToppings) {
    const topping = toppingOptions[Math.floor(Math.random() * toppingOptions.length)];
    if (!toppings.includes(topping)) toppings.push(topping);
}
return pizzaOven(crust, sauce, cheeses, toppings);
}
console.log(randomPizza());
