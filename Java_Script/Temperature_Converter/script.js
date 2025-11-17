const text=document.getElementById("i1");
const cel=document.getElementById("i2");
const far=document.getElementById("i3");
const res=document.getElementById("res");
let temp;

function convert(){
  if(cel.checked){
    temp=Number(text.value);
    temp=temp*1.8+32;
    res.textContent=` ${temp} ° F`;

  }
  else if(far.checked){
    temp=Number(text.value);
    temp=(temp-32)*(1.8);
    res.textContent=`${temp} ° C`
  }
  else{
    res.textContent="Select a unit";
  }
}
