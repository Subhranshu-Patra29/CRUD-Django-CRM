function toggleChat() {
    let chatWindow = document.getElementById("chat-window");
    let chatBody = document.getElementById("chat-body");
    
    if (chatWindow.style.display === "none" || chatWindow.style.display === "") {
        chatWindow.style.display = "flex";
        chatBody.innerHTML = ""; // Clear previous chat history
        showMenu(); // Display menu on chatbot open
    } else {
        chatWindow.style.display = "none";
    }
}

function showMenu() {
    let chatBody = document.getElementById("chat-body");
    chatBody.innerHTML += `
        <div class="chat-bubble bot">
            <strong>Welcome to CRM Assistant! Choose an option:</strong><br>
            1️⃣ Go to Dashboard<br>
            2️⃣ Add a New Record<br>
            3️⃣ Search a Record<br>
            4️⃣ Logout<br>
            <br>Type the option number to continue.
        </div>
    `;
}

function sendMessage(event) {
    if (event.key === "Enter") {
        sendMessageManual();
    }
}

function sendMessageManual() {
    let input = document.getElementById("chat-input").value.trim();
    if (input === "") return;

    let chatBody = document.getElementById("chat-body");
    chatBody.innerHTML += `<div class="chat-bubble user">${input}</div>`;
    chatBody.scrollTop = chatBody.scrollHeight;

    fetch("/chatbot/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;  // Redirect if needed
        } else {
            chatBody.innerHTML += `<div class="chat-bubble bot">${data.reply}</div>`;
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    });

    document.getElementById("chat-input").value = "";
}