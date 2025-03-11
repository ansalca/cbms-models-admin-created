// script.js
const chatWindow = document.querySelector('.chat-window');
const messageInput = document.querySelector('#message-input');
const sendButton = document.querySelector('#send-button');
const chatMessages = document.querySelector('.chat-messages');

sendButton.addEventListener('click', () => {
    const message = messageInput.value.trim();
    if (message !== '') {
        const messageHTML = `<p>${message}</p>`;
        chatMessages.innerHTML += messageHTML;
        messageInput.value = '';
    }
});