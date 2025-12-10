let timeoutId;
function st(){
    timeoutId=setTimeout(()=> window.alert("Hello"),1);
    console.log("Started");
}
function cls(){
    clearTimeout(timeoutId);
    console.log("CLEARED");
}
