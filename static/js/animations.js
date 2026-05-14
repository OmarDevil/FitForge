document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("animate-ready");

    const animatedItems = document.querySelectorAll(`
        .hero-content,
        .form-container,
        .info-box,
        .result-card,
        .workout-card,
        .nutrition-card,
        .progress-card,
        .chat-card,
        .feature-card,
        .step-card,
        .saved-checkin,
        .exercise-item,
        .dashboard-actions .btn
    `);

    animatedItems.forEach((item, index) => {
        item.classList.add("reveal-item");
        item.style.transitionDelay = `${Math.min(index * 60, 420)}ms`;
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.12
    });

    animatedItems.forEach((item) => observer.observe(item));
});