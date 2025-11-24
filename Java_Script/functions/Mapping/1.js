/* Mapping is a function that accepts callback and applies the function 
for each element of an array and returns a new array. */

const num=[1,2,3,4];
const sq=num.map(cube);
const q=num.map(square);
console.log(sq);
console.log(q);
function square(items){
    return `Square of ${items} =${items**2}`;
}

function cube(items){
    return `Cube of ${items}=${items**3}`;
}
