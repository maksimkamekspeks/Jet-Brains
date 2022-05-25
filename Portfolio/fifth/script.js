let appear = document.querySelector(".open-window");
let stopAppear = document.querySelector(".close");
let window = document.querySelector(".window");
let open = document.querySelector(".device_open")
let close = document.querySelector(".device_close")
let menu = document.querySelector(".hamburger")
appear.onclick = function (){
    window.style.display = "run-in";
}
stopAppear.onclick = function (){
    window.style.display = "none";
}
open.onclick = function (){
    open.style.display = "none";
    close.style.display = "run-in";
    menu.style.display = "run-in";
}
close.onclick = function (){
    open.style.display = "run-in";
    close.style.display = "none";
    menu.style.display = "none";
}