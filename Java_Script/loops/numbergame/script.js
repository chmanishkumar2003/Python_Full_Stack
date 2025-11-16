const min=1;
const max=100;
const ans=Math.floor(Math.random()*(max-min+1))+min;

let attempts=0;
let guess;
let running = true;

while(running){
  guess=window.prompt(`Enter a number between ${min}-${max}`);
  guess=Number(guess);
  if (isNaN(guess)){
    window.alert("Please enter a valid number");
  }
  else if(guess < min || guess > max){
    window.alert("Please enter a valid number");
  }
  else{
    attempts++;
    if(guess < ans){
      window.alert("you are very low,Try again!");
    }
    else if(guess > ans){
      window.alert("you are very high,Try again!");
    }
    else{
      window.alert(`Correct! you got right answer in ${attempts} attempts`);
      running = false;
    }
  }
  
}
