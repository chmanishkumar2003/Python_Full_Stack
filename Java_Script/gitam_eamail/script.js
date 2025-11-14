const fname = document.getElementById("i1");
const sname = document.getElementById("i3");
const button = document.getElementById("b1");
const res = document.getElementById("res");

button.onclick = function () {
  const first = fname.value.trim().toLowerCase();
  const second = sname.value.trim().toLowerCase();

  if (second.length === 0 || first.length === 0) {
    res.textContent = "❌ Please enter both first name and surname.";
    return;
  }

  // CASE 1: surname >= 8 → Normal username
  if (second.length >= 8) {
    const username = `${first.slice(0, 1)}${second.slice(0, 8)}@gitam.in`;
    res.textContent = `✅ Your username is: ${username}`;
  } 
  
  // CASE 2: surname < 7 → Add random digits until length becomes 7
  else if (second.length < 7) {
    let base = first.slice(0, 1) + second;  // first letter + surname

    while (base.length < 7) {
      base += Math.floor(Math.random() * 10);  // append random digit 0–9
    }

    const username = `${base}@gitam.in`;
    res.textContent = `Your username is: ${username}`;
  }
};
