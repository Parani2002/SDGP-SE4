const chatButton = document.getElementById("chat-button");
const chatContainer = document.getElementById("chatContainer");
const minimizeButton = document.getElementById("minimize-button");
const chatInput = document.getElementById("chat-input");
const chatMessages = document.getElementById("conversation-group");
const sendButton = document.getElementById("SentButton");

function openChatContainer() {
    chatContainer.classList.add("open");
    chatButton.classList.add("clicked");
}

function closeChatContainer() {
    chatContainer.classList.remove("open");
    chatButton.classList.remove("clicked");
}

function createMessage(message, isUser = true) {
    const newMessage = document.createElement('div');
    newMessage.classList.add(isUser ? 'sentText' : 'botText');
    newMessage.textContent = message;
    chatMessages.appendChild(newMessage);
    return newMessage;
}

function chatbotResponse() {
    const messages = ["Hello!", "How can I assist you?", "Let me know if you have any further questions"];
    const randomIndex = Math.floor(Math.random() * messages.length);
    const message = messages[randomIndex];
    const botMessage = createMessage(message, false);
    botMessage.scrollIntoView();
}

function handleInput() {
    sendButton.classList.toggle("svgsent", chatInput.value.trim() !== "");
}

function handleKeyPress(event) {
    if (event.keyCode === 13) {
        sendMessage();
    }
}

function sendMessage() {
    const message = chatInput.value.trim();
    if (message) {
        chatInput.value = "";
        const userMessage = createMessage(message);
        userMessage.scrollIntoView();
        setTimeout(chatbotResponse, 1000);
        sendButton.classList.add("svgsent");
    }
}

function handleSendButtonClick() {
    sendMessage();
}

// Event listeners
if (chatButton) {
    chatButton.addEventListener("click", openChatContainer);
}

if (minimizeButton) {
    minimizeButton.addEventListener("click", closeChatContainer);
}

chatInput.addEventListener("input", handleInput);
chatInput.addEventListener("keypress", handleKeyPress);

if (sendButton) {
    sendButton.addEventListener("click", handleSendButtonClick);
}
