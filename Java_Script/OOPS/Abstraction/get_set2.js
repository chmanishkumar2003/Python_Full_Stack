class User{
    constructor(name,age){
        this.name=name;
        this.age=age;
    }
    set name(newName){
        if(typeof newName === "string" && newName.length > 0){
            this._name=newName;
        }
        else{
            console.log(`${newName} is not a name`);
        }
    }
    get name(){
        return this._name;
    }
    set age(newAge){
        if (typeof newAge === "number" && newAge > 0){
            this._age=newAge;
        }
        else{
            console.log(`${newAge} is not a age`);
        }
    }
    get age(){
        return this._age;
    }
}
const p1 =new User("manish",107);
console.log(p1.name);
console.log(p1.age);
