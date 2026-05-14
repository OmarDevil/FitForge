document.addEventListener("DOMContentLoaded", function () {
    const backBtn = document.getElementById("backButton");
    if (!backBtn) return;

    const currentPath = window.location.pathname;

    if (currentPath === "/") {
        backBtn.style.display = "none";
        return;
    }

    backBtn.addEventListener("click", function () {
        if (window.history.length > 1) {
            window.history.back();
        } else {
            window.location.href = "/";
        }
    });
});