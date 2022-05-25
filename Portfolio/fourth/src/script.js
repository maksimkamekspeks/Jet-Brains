let appear = document.querySelector(".open-window");
let stopAppear = document.querySelector(".close");
let window = document.querySelector(".window");
appear.onclick = function (){
    window.style.display = "run-in";
}
stopAppear.onclick = function (){
    window.style.display = "none";
}