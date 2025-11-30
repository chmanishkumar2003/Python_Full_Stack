class Animal{
    constructor(name,age){
        this.name=name;
        this.age=age;
    }
    move(speed){
        console.log(`The ${this.name} is moving with ${speed}kmph.`);
    }
}
class Fish extends Animal{
    constructor(name,age,swim){
        super(name,age);
        this.swim=swim;
    }
}
class Rabbit extends Animal{
    constructor(name,age,run){
        super(name,age);
        this.run=run;
    }
    runSpeed(){
        console.log(`The ${this.name} can run`);
        super.move(this.run);
    }
}
class Cow extends Animal{
    constructor(name,age,walkSpeed){
        super(name,age);
        this.walkSpeed=walkSpeed;
    }
    walk(){
        console.log(`The ${this.name} can walk`);
        super.move(this.walkSpeed);
    }
}

const rabbit = new Rabbit("Snoopy",1,30);
const fish = new Fish("Meg",10,70);
const cow = new Cow("Rocky",4,20);

console.log(cow.name);
console.log(rabbit.name);
cow.walk();
rabbit.runSpeed();
