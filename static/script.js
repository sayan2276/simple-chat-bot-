async function sendMessage() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) return;

    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class="message user">${msg}</div>`;
    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    chatbox.innerHTML += `<div class="message bot">${data.reply}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}

function checkEnter(event) {
    if (event.key === "Enter") sendMessage();
}
