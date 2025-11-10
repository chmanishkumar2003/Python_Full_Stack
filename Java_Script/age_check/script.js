button.onclick = function() {
    const age = Number(ageInput.value);
    if (age >= 18) {
        window.alert("You can acess this page");
    } else {
        window.alert("You are not 18+");
    }
