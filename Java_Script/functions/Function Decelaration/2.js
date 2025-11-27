const num=[1,2,3,4];
const sq=num.map(function (item){
//Where function is declared as value
    return Math.pow(item,2);
});
const even=num.filter(function (items){
    return items % 2 === 0;
});
const odd=num.filter(function (items){
    return items % 2 !== 0;
});
console.log("The squares are "+ sq);
console.log("The evens are "+ even);
console.log("The odd are "+ odd);
