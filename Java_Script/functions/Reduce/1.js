//Reduce is a function that reduces the elemnts into single element in an array.
const num=[1,2,3,4,5];
const tot=num.reduce(sum);

console.log(`Total of array is ${tot.toFixed(2)}`);
//toFixed() is a in-built function is used to give output of 2 decimal points.

function sum(prv,next){
    return prv+next;
}
