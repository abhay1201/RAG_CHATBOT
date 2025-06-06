document.getElementById('askBtn').addEventListener('click', async () => {
  const question = document.getElementById('questionInput').value;
  const answerBox = document.getElementById('answerBox');
  answerBox.innerHTML = "Thinking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    answerBox.innerHTML = `<strong>Answer:</strong> ${data.answer}`;
  } catch (err) {
    answerBox.innerHTML = "❌ Error getting answer.";
    console.error(err);
  }
});
