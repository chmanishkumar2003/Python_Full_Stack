let num=[1,2,3,4];
num.forEach(cube);
num.forEach(dis);

function tri(elements,i,arr){
    arr[i]=elements*3;
}
function dis(elements){
    console.log(elements);
}
function sqr(elements,i,arr){
    arr[i]=Math.pow(elements,2);
}
function cube(elements,i,arr){
    arr[i]=elements**3;
}
