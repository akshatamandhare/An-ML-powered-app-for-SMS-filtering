// static/script.js

document.addEventListener("DOMContentLoaded", function () {
    const switchInput = document.getElementById("theme-switch");
    const isDark = localStorage.getItem("darkMode") === "true";

    if (isDark) {
        document.body.classList.add("dark-mode");
        switchInput.checked = true;
    }

    switchInput.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", switchInput.checked);
    });
});
