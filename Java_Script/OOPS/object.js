//Object is a collection of related properties and /or methodes 
//          that can represent real world objects(people,products,places)
//          object={key:value, function()}.

//Methods are the functions that belong to the object.
//Object name should be unique it cant be same.
const person={
    fname:"Manish",
    age:20,
    gender:"Male",
    hello:function(){console.log("Hi i am Manish")},
    eat: ()=>{console.log("I am eating Kabab")}
}
console.log(person.age);
person.hello();
person.eat();
