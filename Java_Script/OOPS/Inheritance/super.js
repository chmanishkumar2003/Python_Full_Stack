//Super Keyword is used in classes for calling the constructor or acessing the properties
// and methods of parent class 
//this=this object
//super= the parent
class Animal{
    constructor(name,age){
        this.name=name;
        this.age=age;
    }
}
class Fish extends Animal{
    constructor(name,age,speed){
        super(name,age);
        this.speed=speed;
    }
}
class Rabbit extends Animal{
    constructor(name,age,speed){
        super(name,age);
        this.speed=speed;
    }
}
class Cow extends Animal{
    constructor(name,age,speed){
        super(name,age);
        this.speed=speed;
    }
}

const rabbit = new Rabbit("Snoopy",1,20);
const fish = new Fish("Meg",10,70);
const cow = new Cow("Rocky",4,30);

console.log(cow.name);
console.log(cow.speed);
console.log(rabbit.name);
