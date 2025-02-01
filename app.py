<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Add your CSS styles here */
    </style>
    <title>Healthcare Chatbot</title>
</head>
<body>
    <div id="chat-container">
        <div id="header">Healthcare Chatbot</div>
        <div id="chat-messages"></div>
        <div id="user-input">
            <input type="text" id="user-message" placeholder="Type your symptoms...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            var userMessage = document.getElementById("user-message").value;
            fetch('/process_symptoms', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'symptoms': userMessage })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Response from server:', data);
                // Handle the response from the server if needed
                // For example, display the bot response in the chat window
                displayMessage("Bot", data.response);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

        function displayMessage(sender, message) {
            var chatMessages = document.getElementById("chat-messages");
            var newMessage = document.createElement("div");
            newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
            chatMessages.appendChild(newMessage);

            // Scroll to the bottom of the chat container
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    </script>
</body>
</html>


