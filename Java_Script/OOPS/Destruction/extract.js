//Extract values from objects
const p1={
    user:"Manish",
    age:20,
    loc:"hyd"
}
const p2={
    user:"Manish kum",
    age:22,
    //loc:"yd"
}

const {user,age,loc="S W O E"}= p2;
console.log(user);
console.log(age);
console.log(loc);
