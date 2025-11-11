const ageInput = document.getElementById("i1");
const License = document.getElementById("License");
const b1=document.getElementById("b1");
const output=document.getElementById("p1");

b1.onclick=function(){

    const x=Number(ageInput.value);
    const hasLicense =License.value ==="Yes";
    if (x >= 18) {
    if (hasLicense) {
        output.textContent="You have age for taking license ,And you have your License";
    } else {
        output.textContent="You have age for taking license ,But You didnt take your License";
    }
} else if (x < 0) {
    output.textContent="Your age cant be less than 0";

} else {
    output.textContent="You dont have age to take License";
}

}
