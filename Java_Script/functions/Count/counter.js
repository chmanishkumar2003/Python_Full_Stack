function counter(){
    let num=0;

    function inc(){
        num++;
        console.log(`Count increased to ${num}`);
    }
    function get(){
        return num;
    }
    return{inc,get};
}
const count = counter();
count.inc();
count.inc();
count.inc();
count.inc();

console.log(`The current count is ${count.get()}`);
