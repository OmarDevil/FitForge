const chatForm = document.getElementById("chatForm");
const chatInput = document.getElementById("chatInput");
const chatMessages = document.getElementById("chatMessages");

function addMessage(text, type) {
    const messageDiv = document.createElement("div");
    messageDiv.className = type === "user" ? "user-message" : "bot-message";
    messageDiv.textContent = text;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

if (chatForm) {
    chatForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        const message = chatInput.value.trim();
        if (!message) return;

        addMessage(message, "user");
        chatInput.value = "";

        try {
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            addMessage(data.reply, "bot");
        } catch (error) {
            addMessage("An error occurred while contacting the assistant.", "bot");
        }
    });
}