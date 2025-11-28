//Class provides a more structured and cleaner way to work with objects compared 
// to the functions. Class is a blueprint of objects
//And objects are instances of class
class Product{
    constructor (pname,price){
        this.pname=pname;
        this.price=price;
    }
    display(){
        console.log(`Product: ${this.pname}`);
        console.log(`Price: ${this.price}`);
    }
    total(gst){
        return this.price + (this.price * gst);
    }
}
const gst=0.05;
const pr1=new Product("5 Star",20);
const pr2=new Product("Silk",200);

pr1.display();
const total=pr1.total(gst);
console.log('Total after gst: '+total);
