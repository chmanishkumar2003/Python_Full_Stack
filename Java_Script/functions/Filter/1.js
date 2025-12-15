//Filter function creates a new array by filtering out elements
let num=[1,2,3,4,5,6];
let evenNum=num.filter(odd);

console.log(evenNum);

function even(item){
    return item % 2 ===0;
}
//Function for odd
function odd(item){
    return item % 2!==0;
}
