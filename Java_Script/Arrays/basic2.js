for(i=fruits.length-1;i>=0;i--){
  console.log(fruits[i]);
}//Its prints all fruits without undefined value.

fruits.sort().reverse();
console.log(fruits);


let user="Manish kumar";
user=user.replace(" ","");
let letters=[...user].join("-");//.... is Spread opretors used of sepreation and can also add items.
console.log(letters);
