//Closure = A function declared inside a another function , the inner function has 
// acess to the variables and scope of outer function. 
//Allow for private variables and state maintanence
function game(){

let score=0;
function inc(points){
    score+=points;
    console.log(`+${points}pts`);
}
function dec(points){
    score-=points;
    console.log(`-${points}pts`);
}
function get(){
    return score;
}
    return{inc,dec,get};
}
const obj =game();
obj.inc(9);
obj.dec(2);
console.log(`The final score ${obj.get()}`);
