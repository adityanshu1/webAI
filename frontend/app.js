const input = document.getElementById("input");
const responseBox = document.getElementById("response");

input.addEventListener("keydown", async (e) => {
  if (e.key === "Enter") {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input.value })
    });
    const data = await res.json();
    responseBox.innerText = data.response;
  }
});

