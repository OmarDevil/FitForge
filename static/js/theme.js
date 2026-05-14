const THEME_KEY = "fitforge_theme";

function setTheme(theme) {
    document.body.setAttribute("data-theme", theme);

    const btn = document.getElementById("themeToggle");
    if (btn) {
        btn.textContent = theme === "dark" ? "Light Mode" : "Dark Mode";
    }

    localStorage.setItem(THEME_KEY, theme);
}

function initTheme() {
    const savedTheme = localStorage.getItem(THEME_KEY) || "dark";
    setTheme(savedTheme);

    const btn = document.getElementById("themeToggle");
    if (btn) {
        btn.addEventListener("click", function () {
            const currentTheme = document.body.getAttribute("data-theme") || "dark";
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            setTheme(newTheme);
        });
    }
}

document.addEventListener("DOMContentLoaded", initTheme);