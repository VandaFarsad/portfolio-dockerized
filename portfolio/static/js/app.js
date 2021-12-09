// nav hamburger selections
const burger = document.querySelector("#burger-menu");
const ul = document.querySelector("nav ul");
const nav = document.querySelector("nav");

// select nav links
const navLink = document.querySelectorAll(".nav-link");

// hamburger menu function
burger.addEventListener("click", () => {
  ul.classList.toggle("show");
});

// close hamburger menu when a link is clicked
navLink.forEach((link) =>
  link.addEventListener("click", () => {
    ul.classList.remove("show");
  })
);
