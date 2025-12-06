//Array of objects
const fruits=[{name:"apple",time:5,cal:57},
              {name:"banana",time:7,cal:90},
              {name:"pine",time:3,cal:84},
              {name:"custard",time:4,cal:94}];

fruits.push({name:"mango",time:3,cal:74});
fruits.pop();
fruits.splice(1,2);
console.log(fruits);

//forEach()
fruits.forEach(fruits=> console.log(fruits.name));
fruits.forEach(fruits=> console.log(fruits.cal));
