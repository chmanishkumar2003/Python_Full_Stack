function sum(...num){
    let res=0;
    for(let n of num){
        res+=n;
    }
    return res;
}

const total=sum(1,2,3,45);
console.log(`Your total is ${total}`);
