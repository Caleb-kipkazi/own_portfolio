document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new URLSearchParams(new FormData(this)).toString();
    const responseDiv = document.getElementById('responseMessage');

    responseDiv.innerText = "Processing...";

    fetch('/submit-contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        responseDiv.innerHTML = `<span style="color: #EE6E13">${data}</span>`;
        this.reset();
    })
    .catch(err => {
        responseDiv.innerText = "Error connecting to server.";
    });
});