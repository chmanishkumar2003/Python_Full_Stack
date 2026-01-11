//Destructing = extract values from arrays or obejects ,and the assign them 
//to variables in a convinent way
//[]= to perform array destruction
//{} = to perform object destruction 
//Swapping variables
// let a=1;
// let b=2;
// [a,b]=[b,a]
// console.log(a);
// console.log(b);

//Swapping 2 elements in an array
// const colors=["red","green","black",1,2];
//[colors[0],colors[1]]=[colors[1],colors[0]];
//console.log(colors);

//Assign array elements to the variables
// const colors=["red","green","black",1,2];
// const[c1,c2,c3,...extra]=colors;
// console.log(c3,c1);
// console.log(extra);

//Extract values from objects
// const p1={
//     user:"Manish",
//     age:20,
//     loc:"hyd"
// }
// const p2={
//     user:"Manish kum",
//     age:22,
//     //loc:"yd"
// }

// const {user,age,loc="S W O E"}= p2;
// console.log(user);
// console.log(age);
// console.log(loc);


// Destruction in function parameters
// function display({fn,ln,age,loc="S W O E"}){
//     console.log(`name:${fn} ${ln}`);
//     console.log(`age:${age}`);
//     console.log(`loc:${loc}`);
// }
// const p1={
//     fn:"Manish",
//     ln:"Kumar",
//     age:21,
//     loc:"HYD"
// }
// const p2={
//     fn:"Harish",
//     ln:"Kumar",
//     // loc:"HYD";
// }
// display(p2);


// nested objects = Object enclosed with another objects.
//                  Allowes yo to represent more comlpex data structures
//                  Child object is enclosed by parent object
// example          person(add{},no.{},name{})
//                  cart(mouse{},monitor{},keyboard{})

// const person={
//     fn:"Manish",
//     age:33,
//     hobbies:["Cricket","Games","Sleeping"],
//     loc:{
//         street:"VNK",
//         dis:"NZB",
//         code:503001,
//     }
// }
// console.log(person.fn);
// console.log(person.age);
// console.log(person.hobbies[2]);
// console.log(person.loc.dis);

//nested object using constructors
// class Person{
//     constructor(name,age,...loc){
//         this.name=name;
//         this.age=age;
//         this.loc=new Loc(...loc);
//     }
// }
// class Loc{
//     constructor(street,dis,pin){
//         this.street=street;
//         this.dis=dis;
//         this.pin=pin;
//     }
// }

// const p1 = new Person("Manish",21,"VNK","NZB",503001);
// const p2 = new Person("Harish",21,"VNXC","SDT",503041);

// console.log(p1.name);
// console.log(p1.age);
// console.log(p1.loc);
// console.log(p2.name);
// console.log(p2.loc);


//Array of objects
// const fruits=[{name:"apple",time:5,cal:57},
//               {name:"banana",time:7,cal:90},
//               {name:"pine",time:3,cal:84},
//               {name:"custard",time:4,cal:94}];
// console.log(fruits[3].name);
// console.log(fruits[1].time);
// console.log(fruits[2].cal);

// fruits.push({name:"mango",time:3,cal:74});
// fruits.pop();
// fruits.splice(1,2);
// console.log(fruits);

//forEach()
// fruits.forEach(fruits=> console.log(fruits.name));
// fruits.forEach(fruits=> console.log(fruits.cal));

//map()
// const names=fruits.map(fruit=>fruit.name);
// console.log(names);

// const age=fruits.map(fruit=>fruit.time);
// console.log(age);

// const caliroes=fruits.map(fruit=>fruit.cal);
// console.log(caliroes);

//Filter()
// const gymFruits = fruits.filter(fruits=>fruits.cal < 85);
// console.log(gymFruits);

// //reduce()

// const maxCal =fruits.reduce((max,fruits)=>
//                             fruits.cal > max.cal?
//                             fruits:max);
// console.log(maxCal);


//Sort()= method used to sort elements of an array in place.Sort elements as strings in 
//lexiographic order , not alphabetical order.
//lexicographic =(alphabetic + numbers + symbols) as strings
// let num=[1,2,6,46,5,9,11]
 // num.sort((a,b)=> a-b);//Assending order
// num.sort((a,b)=> b-a);//Assending order
// console.log(num);

// const people=[{name:"Manish",age:30,gpa:7.41},
//               {name:"Harish",age:30,gpa:7.7},
//               {name:"Rhs",age:30,gpa:8.7},
//               {name:"LHS",age:30,gpa:8.5}]
// // people.sort((a,b)=> b.gpa-a.gpa);
// people.sort((a,b)=> a.name.localeCompare(b.name));
// console.log(people);
        

//Fishers-yates algorithm for shuffling cards
// const cards=['A',1,2,3,7,6,5,9,'J','K','Q'];
// shuffle(cards);
// console.log(cards);

// function shuffle(arr){
//     for(let i=arr.length-1;i>0;i--){
//         const ran=Math.floor(Math.random() *(i+1));
//         [arr[i],arr[ran]]=[arr[ran],arr[i]];
//     }
// }


//Date Objects = objects that contain values that represents dates and times . These date 
//              objects can be changed and formatted.

//Date(year,month,day,hour,minute,second,ms
// const date = new Date();
// console.log(date);

// const date = new Date();
// const year = date.getFullYear();
// const mon = date.getMonth();
// const day =date.getDate();
// const hr = date.getHours();
// const min = date.getMinutes();

// console.log(date);
// console.log(day);
// console.log(mon);
// console.log(year);
// console.log(hr);
// console.log(min);


// let count=0;
// count=100;

// function inc(){
//     count++;
//     console.log(`The count is inc to ${count}`);
// }

// inc();
// inc();
// inc();
// inc();


// function counter(){
//     let num=0;

//     function inc(){
//         num++;
//         console.log(`Count increased to ${num}`);
//     }
//     function get(){
//         return num;
//     }
//     return{inc,get};
// }
// const count = counter();
// count.inc();
// count.inc();
// count.inc();
// count.inc();

// console.log(`The current count is ${count.get()}`);


//Closure = A function declared inside a another function , the inner function has 
// acess to the variables and scope of outer function. 
//Allow for private variables and state maintanence
// function game(){

// let score=0;
// function inc(points){
//     score+=points;
//     console.log(`+${points}pts`);
// }
// function dec(points){
//     score-=points;
//     console.log(`-${points}pts`);
// }
// function get(){
//     return score;
// }
//     return{inc,dec,get};
// }
// const obj =game();
// obj.inc(9);
// obj.dec(2);
// console.log(`The final score ${obj.get()}`);


//setTimeout()= fun in js that allows you to shedule the execution of a function after a
// certain amount of time (all in milliseconds).
//setTimeout(callback,delay);
//clearTimeout(timeoutId)= can cancel timeout before it trigers.

// function hello(){
//     window.alert(`Hello`);
// } 
// setTimeout(hello,3000);
// setTimeout(()=> window.alert(`hello`),3000);
// setTimeout(function(){window.alert(`Hello`)},3000);


// let timeoutId;
// function st(){
//     timeoutId=setTimeout(()=> window.alert("Hello"),1);
//     console.log("Started");
// }
// function cls(){
//     clearTimeout(timeoutId);
//     console.log("CLEARED");
// }


function update(){
    const now = new Date();
    let hrs = now.getHours();
    const mer= hrs >= 12 ? "PM" :"AM";
    hrs = hrs % 12 || 12;
    hrs=hrs.toString().padStart(2,0);
    const min = now.getMinutes().toString().padStart(2,0);
    const sec = now.getSeconds().toString().padStart(2,0);
    const string= `${hrs}:${min}:${sec} ${mer}`;
    document.getElementById("clock").textContent=string;
}
update();
setInterval(update,1000);