const dis = document.getElementById("dis");
let timer = null;
let st = 0;
let et = 0;
let isRun = false;


function start(){
    if (!isRun){
        st= Date.now() - et;
        timer= setInterval(update,10);
        isRun=true;
    }
}
function stop(){
    if(isRun){
        clearInterval(timer);
        et=Date.now() - st;
        isRun=false;
    }
}
function reset(){
    clearInterval(timer);
    st = 0;
    et = 0;
    isRun = false;
    dis.textContent="00:00:00:00";
}
function update() {
    const ct = Date.now();
    et = ct - st;

    let hrs = Math.floor(et / (1000 * 60 * 60));
    let min = Math.floor((et / (1000 * 60)) % 60);
    let sec = Math.floor((et / 1000) % 60);
    let mil = Math.floor((et % 1000) / 10);

    hrs = String(hrs).padStart(2, "0");
    min = String(min).padStart(2, "0");
    sec = String(sec).padStart(2, "0");
    mil = String(mil).padStart(2, "0");

    dis.textContent = `${hrs}:${min}:${sec}:${mil}`;
}
