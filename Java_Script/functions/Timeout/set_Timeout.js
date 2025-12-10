//setTimeout()= fun in js that allows you to shedule the execution of a function after a
// certain amount of time (all in milliseconds).
//setTimeout(callback,delay);
//clearTimeout(timeoutId)= can cancel timeout before it trigers.

function hello(){
    window.alert(`Hello`);
} 
setTimeout(hello,3000);
setTimeout(()=> window.alert(`hello`),3000);
setTimeout(function(){window.alert(`Hello`)},3000);
