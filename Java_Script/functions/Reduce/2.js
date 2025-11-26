const num=[11,22,33,4,55,66];
const min=num.reduce(max);
console.log(min);

function minu(prv,next){
    return Math.min(prv,next);
}
function max(prv,next){
    return Math.max(prv,next);
}
