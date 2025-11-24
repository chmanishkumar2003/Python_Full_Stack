let words=["apple","banana","prompt","Man"];
let short=words.filter(shorter);
let long=words.filter(longer);

console.log(short);
console.log(long);

function shorter(item){
    return item.length <= 5;
}

function longer(item){
    return item.length >=6;
}
