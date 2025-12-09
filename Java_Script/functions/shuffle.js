//Fishers-yates algorithm for shuffling cards
const cards=['A',1,2,3,7,6,5,9,'J','K','Q'];
shuffle(cards);
console.log(cards);

function shuffle(arr){
    for(let i=arr.length-1;i>0;i--){
        const ran=Math.floor(Math.random() *(i+1));
        [arr[i],arr[ran]]=[arr[ran],arr[i]];
    }
}
