async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">You: ${message}</div>`;

    let response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: message })
    });

    let data = await response.json();

    chatBox.innerHTML += `<div class="bot">Bot: ${data.response}</div>`;

    input.value = "";
}