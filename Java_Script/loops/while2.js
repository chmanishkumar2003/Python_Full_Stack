let login=true;
let user;
let pass;

while(!login){
  user=window.prompt("Enter username");
  pass=window.prompt("Enter password");

  if(user==="Manish" && pass==="Manish@123"){
    login=true;
    console.log("You are logged in !");
  }
  else{
    console.log("Invalid Credentials!Please try again");
  }
}
