const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

// Replace with your OpenAI API key
const API_KEY = "";

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  // Display user message
  displayMessage(message, "user-message");

  // Clear input field
  userInput.value = "";

  // Fetch bot response
  const response = await getBotResponse(message);
  displayMessage(response, "bot-message");
}

function displayMessage(message, className) {
  const messageElement = document.createElement("div");
  messageElement.className = `chat-message ${className}`;
  messageElement.textContent = message;
  chatBox.appendChild(messageElement);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

async function getBotResponse(userInput) {
  const prompt = `
    You are a compassionate mental health chatbot named MindCare. Your role is to provide empathetic, thoughtful, and non-judgmental responses to users seeking guidance or support for their mental health. Always encourage them to seek professional help if needed.

    User: ${userInput}
    MindCare:
  `;

  try {
    const response = await fetch("https://api.openai.com/v1/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify({
        model: "text-davinci-003",
        prompt: prompt,
        max_tokens: 200,
        temperature: 0.7,
        top_p: 0.9,
        frequency_penalty: 0.5,
        presence_penalty: 0.6,
      }),
    });

    const data = await response.json();
    return data.choices[0].text.trim();
  } catch (error) {
    console.error("Error:", error);
    return "Sorry, I encountered an issue while processing your request. Please try again later.";
  }
}
