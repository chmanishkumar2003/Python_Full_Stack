//Getter is the special method that makes a property redable.
//setter is the special method that makes a property writeable. 

class Rec{
    constructor(h,w){
        this.h=h;
        this.w=w;
    }
    set w(newWidth){
        if(newWidth > 0){
            this._w=newWidth.toFixed(1);
        }
        else{
            console.log("Width must be positive");
        }
    }
    get w(){
        return this._w;
    }
    set h(newHeight){
        if(newHeight > 0){
            this._h=newHeight.toFixed(1);
        }
        else{
            console.log("Height must be positive");
        }
    }
    get h(){
        return this._h;
    }
    get area(){
        return (this._h * this._w).toFixed(1);
    }   
}
const rect = new Rec(5,6);
console.log(rect.w);
console.log(rect.h);
console.log(rect.area);
