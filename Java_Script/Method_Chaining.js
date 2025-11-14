//Method Chaining in js
//======No Method Chaining =====
let user=window.prompt("Enter name");
user=user.trim();
let letter=user.charAt(0);
letter=letter.toUpperCase();

let extra=user.slice(1);
extra=extra.toLowerCase();
user=letter+extra;
console.log(user);

//Using Method Chaining

username=user.trim().charAt(0).toUpperCase() + user.trim().slice(1).toLowerCase();
console.log(username);
