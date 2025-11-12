const check= document.getElementById("i1");
const card= document.getElementById("i2");
const phpay= document.getElementById("i3");
const paytm= document.getElementById("i4");
const Submit= document.getElementById("b1");
const output= document.getElementById("subres");
const result= document.getElementById("payres");

Submit.onclick=function(){
    if(check.checked){
        output.textContent="You are subscribed !";
    }
    else{
        output.textContent="You are not Subscribed !"
    }
    if(card.checked){
        result.textContent="Done payment with Card!"
    }
    else if(phpay.checked){
        result.textContent="Done payment with Phone Pay!"
    }
    else if(paytm.checked){
        result.textContent="Done payment with Paytm !"
    }
    else{
        result.textContent="Didnt Done payment yet!"
    }
}
