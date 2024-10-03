// Copy the link to the note
document.getElementById('copyLink').addEventListener('click', function(e) {
    e.preventDefault();
    const noteLink = window.location.href;

    navigator.clipboard.writeText(noteLink).then(() => {
        alert('Note link copied to clipboard!');
    }).catch(err => {
        alert('Failed to copy note link.');
    });
});

// Share on WhatsApp
document.getElementById('shareWhatsApp').addEventListener('click', function(e) {
    e.preventDefault();
    const noteLink = window.location.href;
    const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(noteLink)}`;
    window.open(whatsappUrl, '_blank');
});
