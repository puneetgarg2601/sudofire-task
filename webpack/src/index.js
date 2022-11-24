import app from "./assets/app";
import Image from "./images/pexels-craig-adderley-1563355.jpg";

console.log("In index.js");
const img = document.createElement("img");
// const myIcon = new Image();
// myIcon.src = Image;
console.log(Image);
img.setAttribute("src", Image);
img.setAttribute("width", "200px");
img.setAttribute("height", "200px");
document.body.appendChild(img);
const h = document.createElement("h2");
h.textContent = "This is new";
document.body.appendChild(h);
app();
