// script.js

document.getElementById('callbackForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch('/submit_callback_request', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.getElementById('callbackMessageContainer');
        messageContainer.innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
