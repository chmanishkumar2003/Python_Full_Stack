//Constructor is a special method for defining the properties and methods of objects.
function Car(model,year,color){
    this.model=model,
    this.year=year,
    this.color=color,
    this.drive =function(){console.log(`You have to drive the ${this.model} car of year ${this.year}.`)}
}

const car1=new Car("BMW",2019,"Black");
const car2=new Car("BENZ",2019,"Black");
const car3=new Car("Mahindra",2019,"Black");

car3.drive();
