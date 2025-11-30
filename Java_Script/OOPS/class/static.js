
//Static Keyword that defines properties or methods that belong to the class itself
//rather than the objects created from that class.
class Math{
    static PI=3.1421;

    static dia(r){
        return r * 2;
    }
    static area(r){
        return 2 * this.PI * r;
    }
}
console.log(Math.PI);
console.log(Math.dia(10));
console.log(Math.area(10));
