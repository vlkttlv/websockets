const userItems = document.querySelectorAll('.user-item');
const chatTitle = document.querySelector('.chat-title');
const chatArea = document.querySelector('.chat-area');
const noChatSelected = document.querySelector('.no-chat-selected');

userItems.forEach(item => {
    item.addEventListener('click', () => {
        userItems.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
        const userName = item.dataset.name;
        chatTitle.textContent = `Чат с ${userName}`;
        noChatSelected.style.display = 'none';
        chatArea.classList.add('active');
    });
});

const messageInput = document.querySelector('.message-input');
const sendButton = document.querySelector('.send-btn');
const chatMessages = document.querySelector('.chat-messages');

function sendMessage() {
    const message = messageInput.value.trim();
    if (message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', 'sent');
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        messageInput.value = '';
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

document.querySelector('.logout-btn').addEventListener('click', () => {
    window.location.href = 'https://example.com/login';
});