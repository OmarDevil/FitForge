const form = document.getElementById("progressForm");
const summaryBox = document.getElementById("progressSummary");
const checkinsList = document.getElementById("checkinsList");
const chartCanvas = document.getElementById("weightChart");

const STORAGE_KEY = "fitforge_progress_data";
let weightChart = null;

function getCheckins() {
    const data = localStorage.getItem(STORAGE_KEY);
    return data ? JSON.parse(data) : [];
}

function saveCheckins(checkins) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(checkins));
}

function sortCheckins(checkins) {
    return checkins.sort((a, b) => new Date(a.date) - new Date(b.date));
}

function renderSummary(checkins) {
    if (checkins.length === 0) {
        summaryBox.innerHTML = "<p>No progress data yet.</p>";
        return;
    }

    const first = checkins[0];
    const last = checkins[checkins.length - 1];

    const weightChange = (last.weight - first.weight).toFixed(1);
    const waistChange = first.waist && last.waist ? (last.waist - first.waist).toFixed(1) : "N/A";
    const consistency = last.consistency ? `${last.consistency}%` : "N/A";

    summaryBox.innerHTML = `
        <p><strong>First Check-In:</strong> ${first.date}</p>
        <p><strong>Latest Check-In:</strong> ${last.date}</p>
        <p><strong>Starting Weight:</strong> ${first.weight} kg</p>
        <p><strong>Current Weight:</strong> ${last.weight} kg</p>
        <p><strong>Weight Change:</strong> ${weightChange} kg</p>
        <p><strong>Waist Change:</strong> ${waistChange} cm</p>
        <p><strong>Latest Consistency:</strong> ${consistency}</p>
    `;
}

function renderCheckins(checkins) {
    if (checkins.length === 0) {
        checkinsList.innerHTML = "<p>No check-ins saved yet.</p>";
        return;
    }

    checkinsList.innerHTML = checkins
        .map(
            (item, index) => `
            <div class="saved-checkin">
                <div>
                    <h3>Check-In ${index + 1}</h3>
                    <p><strong>Date:</strong> ${item.date}</p>
                    <p><strong>Weight:</strong> ${item.weight} kg</p>
                    <p><strong>Waist:</strong> ${item.waist || "-"} cm</p>
                    <p><strong>Chest:</strong> ${item.chest || "-"} cm</p>
                    <p><strong>Arm:</strong> ${item.arm || "-"} cm</p>
                    <p><strong>Thigh:</strong> ${item.thigh || "-"} cm</p>
                    <p><strong>Consistency:</strong> ${item.consistency || "-"}%</p>
                </div>
                <button class="delete-btn" onclick="deleteCheckin(${index})">Delete</button>
            </div>
        `
        )
        .join("");
}

function renderChart(checkins) {
    if (!chartCanvas) return;

    const labels = checkins.map(item => item.date);
    const weights = checkins.map(item => item.weight);

    if (weightChart) {
        weightChart.destroy();
    }

    weightChart = new Chart(chartCanvas, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Weight (kg)",
                    data: weights,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "white"
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "white"
                    },
                    grid: {
                        color: "rgba(255,255,255,0.08)"
                    }
                },
                y: {
                    ticks: {
                        color: "white"
                    },
                    grid: {
                        color: "rgba(255,255,255,0.08)"
                    }
                }
            }
        }
    });
}

function renderAll() {
    const checkins = sortCheckins(getCheckins());
    renderSummary(checkins);
    renderCheckins(checkins);
    renderChart(checkins);
}

function deleteCheckin(index) {
    const checkins = sortCheckins(getCheckins());
    checkins.splice(index, 1);
    saveCheckins(checkins);
    renderAll();
}

if (form) {
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const newCheckin = {
            date: document.getElementById("date").value,
            weight: parseFloat(document.getElementById("weight").value),
            waist: document.getElementById("waist").value,
            chest: document.getElementById("chest").value,
            arm: document.getElementById("arm").value,
            thigh: document.getElementById("thigh").value,
            consistency: document.getElementById("consistency").value
        };

        const checkins = getCheckins();
        checkins.push(newCheckin);
        saveCheckins(sortCheckins(checkins));
        form.reset();

        document.getElementById("date").value = new Date().toISOString().split("T")[0];

        renderAll();
    });
}

window.addEventListener("load", function () {
    const dateInput = document.getElementById("date");
    if (dateInput && !dateInput.value) {
        dateInput.value = new Date().toISOString().split("T")[0];
    }

    renderAll();
});