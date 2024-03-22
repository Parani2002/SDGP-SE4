// Selecting elements
const body = document.querySelector("body");
const sidebar = document.querySelector(".sidebar");
const toggle = document.querySelector(".toggle");
const modeSwitch = document.querySelector(".toggle-switch");
const modeText = document.querySelector(".mode-text");
const searchBtn = document.querySelector(".search-bar");

// Dark mode toggle
modeSwitch.addEventListener("click", () => {
  body.classList.toggle("dark");
  modeText.textContent = body.classList.contains("dark")
    ? " Light Mode "
    : " Dark Mode ";
});

// Sidebar hover open/close
sidebar.addEventListener("mouseenter", () => {
  sidebar.classList.remove("close");
});

sidebar.addEventListener("mouseleave", () => {
  sidebar.classList.add("close");
});

// Handling search button click to open sidebar
searchBtn.addEventListener("click", () => {
  sidebar.classList.remove("close");
});
