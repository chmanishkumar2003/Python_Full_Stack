
const dec = document.getElementById("dec");
const res = document.getElementById("res");
const inc = document.getElementById("inc");
const label = document.getElementById("l1");


let count = 0;
inc.onclick = function() {
    count++;
    l1.textContent = count;

}

dec.onclick = function() {
    count--;
    l1.textContent = count;
}
res.onclick = function() {
    count = 0;
    l1.textContent = count;
}
