let fruits=["apple","banana","orange","bigan"];
fruits.pop()
fruits.unshift("man");
console.log(fruits);
let index=fruits.indexOf("apple");
console.log(index);
console.log(fruits.length);

for(i=0;i<fruits.length;i++){
  console.log(fruits[i])
}

for(i=fruits.length;i>=0;i--){
  console.log(fruits[i]);
}//Its prints all fruits also undefined because i=4 it is beyond limit of array.

for(i=fruits.length-1;i>=0;i--){
  console.log(fruits[i]);
}//Its prints all fruits without undefined value.
