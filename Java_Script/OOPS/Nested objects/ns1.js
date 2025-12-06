// nested objects = Object enclosed with another objects.
//                  Allowes yo to represent more comlpex data structures
//                  Child object is enclosed by parent object
// example          person(add{},no.{},name{})
//                  cart(mouse{},monitor{},keyboard{})

const person={
    fn:"Manish",
    age:33,
    hobbies:["Cricket","Games","Sleeping"],
    loc:{
        street:"VNK",
        dis:"NZB",
        code:503001,
    }
}
console.log(person.fn);
console.log(person.age);
console.log(person.hobbies[2]);
console.log(person.loc.dis);
