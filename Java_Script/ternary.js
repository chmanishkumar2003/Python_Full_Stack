let age=1;
let message=age>=18? "You are eligible":"You are not eligible";
console.log(message);

let student=true;
let m=student?"You are Student": "You are not a student";
console.log(m);

let amount=110;
let discount=amount>=100? 10:0;
console.log(`Your total bill $${amount-amount*(discount/100)}`);
