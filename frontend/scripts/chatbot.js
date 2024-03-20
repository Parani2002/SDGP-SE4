document.addEventListener('DOMContentLoaded', function() {
    // Function to send a message
    function sendMessage() {
        var input = document.getElementById('chatbot-input');
        var message = input.value.toLowerCase();
        input.value = '';

        var messages = document.getElementById('chatbot-messages');
        messages.innerHTML += '<p>You: ' + message + '</p>';

        // Basic response logic
        setTimeout(function() {
            if (message.includes('hi') || message.includes('hello')) {
                messages.innerHTML += '<p>Chatbot: Hello! How can I help you today?</p>';
            } else {
                messages.innerHTML += '<p>Chatbot: I\'m here to help!</p>';
            }
            messages.scrollTop = messages.scrollHeight;
        }, 1000);
    }

    // Event listener for the chatbot button to open the chatbot popup
    document.getElementById('chatbot-button').addEventListener('click', function() {
        var chatPopup = document.getElementById('chatbot-popup');
        if (chatPopup.style.display === 'none') {
            chatPopup.style.display = 'block';
        } else {
            chatPopup.style.display = 'none';
        }
    });

    // Event listener for the send button to send a message
    document.getElementById('chatbot-send').addEventListener('click', function() {
        sendMessage();
    });

    // Event listener for the Enter key press to send a message
    document.getElementById('chatbot-input').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // Event listener for the close button to close the chatbot popup
    document.getElementById('chatbot-close').addEventListener('click', function() {
        document.getElementById('chatbot-popup').style.display = 'none';
    });

    // Event listener for the Escape key to close the chatbot popup
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            var chatPopup = document.getElementById('chatbot-popup');
            if (chatPopup.style.display !== 'none') {
                chatPopup.style.display = 'none';
            }
        }
    });
});
