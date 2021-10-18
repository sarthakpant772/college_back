const navToggle=document.querySelector(".mobile-nav");
const links=document.querySelector(".nav-button");

navToggle.addEventListener("click",function(){
    links.classList.toggle("show-links");
});