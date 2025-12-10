function update(){
    const now = new Date();
    const hrs = now.getHours().toString().padStart(2,0);
    const min = now.getMinutes().toString().padStart(2,0);
    const sec = now.getSeconds().toString().padStart(2,0);
    const string= `${hrs}:${min}:${sec}`;
    document.getElementById("clock").textContent=string;
}
update();
setInterval(update,1000);
