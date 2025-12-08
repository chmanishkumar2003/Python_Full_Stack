//Sort()= method used to sort elements of an array in place.Sort elements as strings in 
//lexiographic order , not alphabetical order.
//lexicographic =(alphabetic + numbers + symbols) as strings
// let num=[1,2,6,46,5,9,11]
 // num.sort((a,b)=> a-b);//Assending order
// num.sort((a,b)=> b-a);//Assending order
// console.log(num);

const people=[{name:"Manish",age:30,gpa:7.41},
              {name:"Harish",age:30,gpa:7.7},
              {name:"Rhs",age:30,gpa:8.7},
              {name:"LHS",age:30,gpa:8.5}]
// people.sort((a,b)=> b.gpa-a.gpa);
people.sort((a,b)=> a.name.localeCompare(b.name));
console.log(people);
        
