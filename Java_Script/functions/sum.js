// ... is the Rest parameter which is used for collection of all arguments into an array.
function sum(...num){
    let res=0;
    for(let n of num){
        res+=n;
    }
    return res;
}

const total=sum(1,2,3,45);
// Here "1,2,3,45" is the value passed to the function as num parameter.
console.log(`Your total is ${total}`);

