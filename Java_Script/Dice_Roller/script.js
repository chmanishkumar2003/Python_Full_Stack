function roll() {
    const num = document.getElementById("i1").value;
    const res = document.getElementById("res");
    const img = document.getElementById("img");
// Const elements cant be changed
    const val = [];
    const image = [];

    for (let i = 0; i < num; i++) {
        const value = Math.floor(Math.random() * 6) + 1;
        val.push(value);
        image.push(`<img src="dice/${value}.jpg" width="100">`);
    }

    res.textContent = `dice: ${val.join(", ")}`;
    img.innerHTML = image.join('');
}
