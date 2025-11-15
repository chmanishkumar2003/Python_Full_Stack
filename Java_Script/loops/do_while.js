do while it firsts does the code and checks the condition.
let u;
do{
  u=window.prompt("Enter User Name");
}
while(u==="" || u===null)
console.log(`Hello ${u}`);
