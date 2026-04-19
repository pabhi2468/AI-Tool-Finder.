async function searchTools() {
  const query = document.getElementById("query").value.trim();
  const messagesDiv = document.getElementById("chat-messages");
  const loader = document.getElementById("loader");
  const button = document.getElementById("search-btn");

  if (!query) return;

  // Show loading spinner and disable button
  loader.style.display = "block";
  button.style.display = "none";
  button.disabled = true;

  messagesDiv.innerHTML += `<div class="user-message"><strong>You:</strong> ${query}</div>`;

  try {
    const response = await fetch("/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    const data = await response.json();
    console.log('data: ', data)
    messagesDiv.innerHTML += `<div class="bot-message">${data?.tools || data?.response}</div>`;
  } catch (error) {
    messagesDiv.innerHTML += `<div class="bot-message error">Error fetching data.</div>`;
  }

  loader.style.display = "none";
  button.disabled = false;
  button.style.display = "block";
  document.getElementById("query").value = "";
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}