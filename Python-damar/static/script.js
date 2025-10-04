document.addEventListener('DOMContentLoaded', function() {
    // Tombol fakta acak
    const factButton = document.getElementById('fact-button');
    const factText = document.getElementById('fact-text');
    
    if (factButton && factText) {
        factButton.addEventListener('click', function() {
            fetch('/api/random-fact')
                .then(response => response.json())
                .then(data => {
                    factText.textContent = data.fact;
                })
                .catch(error => {
                    factText.textContent = 'Gagal mengambil fakta. Silakan coba lagi.';
                    console.error('Error:', error);
                });
        });
    }
    
    // Animasi untuk card
    const cards = document.querySelectorAll('.feature-card, .project-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
    });
});