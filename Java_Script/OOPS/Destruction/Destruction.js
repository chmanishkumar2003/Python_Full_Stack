//Destruction in function parameters
function display({fn,ln,age,loc="S W O E"}){
    console.log(`name:${fn} ${ln}`);
    console.log(`age:${age}`);
    console.log(`loc:${loc}`);
}
const p1={
    fn:"Manish",
    ln:"Kumar",
    age:21,
    loc:"HYD"
}
const p2={
    fn:"Harish",
    ln:"Kumar",
    // loc:"HYD";
}
display(p2);
