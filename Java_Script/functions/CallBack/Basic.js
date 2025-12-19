//Callback is a function that is passed as argument in another function
/*It is used for asychronous operations
        1)Reading files
        2)Iterating with data bases
        3)Network Requests*/

sum(display,1,2);

function sum(call,x,y){
    let res=x+y;
    call(res);
}
//Call back sum function
function display(res){
    document.getElementById("h1").textContent=res;
}
