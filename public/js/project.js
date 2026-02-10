const projectDetails = {
    scrap: {
        title: "Waste Management Web Engine",
        tech: "Python, JavaScript, PostgreSQL",
        impact: "Optimized collection routes by 30% and digitized 100% of payment tracking."
    },
    mobile: {
        title: "Scrap Connect Mobile App",
        tech: "React Native, Node.js, Firebase",
        impact: "Enabled real-time communication between 500+ collectors and households."
    },
    dashboard: {
        title: "Performance Analytics",
        tech: "D3.js, HTML5, Vanilla CSS",
        impact: "Visualized over 10k+ requests for city-wide waste management reporting."
    }
};

function showDetails(key) {
    const project = projectDetails[key];
    const modal = document.getElementById('projectModal');
    const content = document.getElementById('modalContent');

    content.innerHTML = `
        <h2 style="color: #EE6E13">${project.title}</h2>
        <p style="color: #888; margin: 15px 0;"><strong>Technologies:</strong> ${project.tech}</p>
        <p style="color: #eee; line-height: 1.6;">${project.impact}</p>
        <button class="btn-fill" style="margin-top: 20px;" onclick="closeModal()">Got it</button>
    `;

    modal.style.display = 'block';
}

function closeModal() {
    document.getElementById('projectModal').style.display = 'none';
}

// Close when clicking outside the box
window.onclick = function(event) {
    const modal = document.getElementById('projectModal');
    if (event.target == modal) {
        closeModal();
    }
}