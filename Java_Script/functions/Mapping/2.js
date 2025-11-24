const dates=["2024-11-12","2024-11-11","2024-24-11"];
const real=dates.map(formal);

console.log(real);
function formal(items){
    const parts=items.split("-");
    return `${parts[1]}/${parts[2]}/${parts[0]}`;
}
