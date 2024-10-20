// Toggle between dark and light mode
function toggleMode() {
    document.body.classList.toggle('light-mode');
    const modeToggle = document.getElementById('modeToggle');
    modeToggle.textContent = document.body.classList.contains('light-mode') ? '☀️' : '🌙';
}

// Send a message from the user
function sendMessage(message = null) {
    const messageInput = document.getElementById('messageInput');
    const userMessage = message || messageInput.value;

    if (!userMessage) return;

    // Display the user's message
    displayMessage('user', userMessage);

    // Send the message to the backend API
    fetch('/api/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure CSRF token for POST request
        },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        displayMessage('bot', data.bot_response);
        messageInput.value = ''; // Clear the input field
    })
    .catch(error => console.error('Error:', error));
}

// Display a message on the chat screen
function displayMessage(sender, message) {
    const chatBox = document.querySelector('.chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);

    const avatar = document.createElement('span');
    avatar.classList.add('avatar');
    avatar.textContent = (sender === 'bot') ? '🤖' : '👤';

    const text = document.createElement('p');
    text.textContent = message;

    messageElement.appendChild(avatar);
    messageElement.appendChild(text);

    chatBox.appendChild(messageElement);

    // Automatically scroll to the bottom of the chat
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Handle the card selection and send predefined messages
document.querySelectorAll('.options button').forEach(button => {
    button.addEventListener('click', function () {
        const question = button.textContent.trim();  // Get the text of the button
        sendMessage(question);  // Send the predefined question
    });
});

// Listen for the "Enter" keypress on the message input field
document.getElementById('messageInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevents the default behavior of the Enter key (like form submission)
        sendMessage();  // Trigger sending the message
    }
});

// Function to get the CSRF token for POST requests
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Handle file upload
document.getElementById('attachButton').addEventListener('click', function () {
    const fileInput = document.getElementById('fileInput');
    fileInput.click();  // Trigger the hidden file input
});

document.getElementById('fileInput').addEventListener('change', function () {
    uploadFile();  // Call the upload function when a file is selected
});

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        return;
    }

    // Display the file in the chat as a user message
    displayMessage('user', `File: ${file.name}`);

    const formData = new FormData();
    formData.append('file', file);

    // Send the file to the backend API
    fetch('/api/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Display confirmation in chat
            displayMessage('bot', `File uploaded: ${file.name}`);
        } else {
            console.error('File upload failed:', data.error);
        }
    })
    .catch(error => console.error('File upload error:', error));

    // Clear the file input after uploading
    fileInput.value = '';
}
