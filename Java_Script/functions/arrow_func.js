/* Arrow functions are used to write function in shorter and cleaner way.  */
const num =[1,2,3,4,5];
const sq= num.map((item)=>Math.pow(item,2));
const cubes= num.map((item)=>Math.pow(item,3));
const even= num.filter((item)=> item%2===0);
const odd= num.filter((item)=> item%2!==0);

console.log(sq);
console.log(cubes);
console.log(odd);
console.log(even);
