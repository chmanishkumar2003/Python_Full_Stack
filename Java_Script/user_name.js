let user;
user = window.prompt("What is name/username ? ")
console.log(user);

document.getElementById("s1").onclick = function() {
    user = document.getElementById("u1").value;
    user = document.getElementById("h1").textContent = "Hello " + user;
    console.log(user);
}
