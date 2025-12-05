//nested object using constructors
class Person{
    constructor(name,age,...loc){
        this.name=name;
        this.age=age;
        this.loc=new Loc(...loc);
    }
}
class Loc{
    constructor(street,dis,pin){
        this.street=street;
        this.dis=dis;
        this.pin=pin;
    }
}

const p1 = new Person("Manish",21,"VNK","NZB",503001);
const p2 = new Person("Harish",21,"VNXC","SDT",503041);

console.log(p1.name);
console.log(p1.age);
console.log(p1.loc);
console.log(p2.name);
console.log(p2.loc);
