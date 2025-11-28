//This keywrod is used for reference of current context.
It varies by how and where code is executed
const person={
    fname:"Manish",
    age:20,
    gender:"Male",
    food :"Kabab",
    hello:function(){console.log("Hi i am "+person.fname)},
    eat: function(){console.log("I am eating "+person.food)}
}
console.log(person.age);
person.hello();
person.eat();
