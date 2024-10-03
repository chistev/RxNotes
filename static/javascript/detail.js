// Copy the note content
document.getElementById('copyNote').addEventListener('click', function(e) {
    e.preventDefault();
    const noteContentElement = document.getElementById('noteContent');
    
    // Create a temporary textarea to copy the content
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = noteContentElement.textContent; // Use textContent for plain text
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    
    try {
        document.execCommand('copy');
        alert('Note content copied to clipboard!');
    } catch (err) {
        alert('Failed to copy note content.');
    }
    
    document.body.removeChild(tempTextArea); // Clean up
});

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
