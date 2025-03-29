document.getElementById("myForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const formData = new formData(this);

    // Send data to backend
    await fetch("/submit", {
        method: "POST",
        body: formData
    });

    // Refresh displayed submissions
    loadSubmissions();
});

async function loadSubmissions() {
    const response = await fetch("/submissions");
    const data = await response.json();
    document.getElementById("submissions").innerHTML = data.map(entry => 
    <p><strong>${entry.title}:</strong> <br /> <i>${entry.themes}</i> <br /> ${entry.confession} <br /> ${entry.author_info}</p>).join("");
}

// Load submissions when the page loads
loadSubmissions();