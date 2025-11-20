function generate(length, low, upp, num, sym) {
    const lower = "abcdefghijklmnopqrstuvwxyz";
    const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const number = "0123456789";
    const symbol = "!@#$%&*_-+";

    let afterF = "";
    if (low) afterF += lower;
    if (num) afterF += number;
    if (sym) afterF += symbol;

    const firstCharSet = upper;

    if (length < 1) return "(Password length must be at least 1)";
    if (afterF.length === 0) return "(At least lowercase, number, or symbol must be enabled)";

    let pass = "";
    pass += firstCharSet[Math.floor(Math.random() * firstCharSet.length)];

    for (let i = 1; i < length; i++) {
        const random = Math.floor(Math.random() * afterF.length);
        pass += afterF[random];
    }

    return pass;
}

const length = 8;
const low = true;
const upp = true;
const num = true;
const sym = true;

const pass = generate(length, low, upp, num, sym);
console.log("Your Generated Password: " + pass);
