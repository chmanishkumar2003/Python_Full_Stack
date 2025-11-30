//Inheritnce allows a new class to inhertit methods of excisting class
//parent-> child class and child class can have their own/unique methods.

class Animal{
    alive=true;
    sleep(){
        console.log(`This ${this.name} is sleeping`);
    }
    eat(){
        console.log(`This ${this.name} is eating`);
    }
}
class Rabit extends Animal{
    name="rabbit";
    run(){
        console.log("The "+this.name+" is running");
    }
}
class Cow extends Animal{
    name="cow";
}
const rabbit = new Rabit();
rabbit.sleep();
rabbit.alive=false;
rabbit.run();

const cow = new Cow();
cow.sleep();
cow.eat();
console.log(rabbit.alive);
