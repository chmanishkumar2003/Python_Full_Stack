let fr=["apple","banana","mango"];

fr.forEach(cap);
fr.forEach(dis);

function upp(items,i,arr){
    arr[i]=items.toUpperCase();
}

function cap(items,i,arr){
    arr[i]=items.charAt(0).toUpperCase() + items.slice(1);
}
function dis(items){
    console.log(items);
}
