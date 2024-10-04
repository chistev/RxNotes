document.addEventListener('DOMContentLoaded', function () {
    const copyLink = document.getElementById('copyLink');
    const shareWhatsApp = document.getElementById('shareWhatsApp');
    
    console.log('Copy link element:', copyLink);  // Debugging logs to check if elements exist
    console.log('WhatsApp share element:', shareWhatsApp);

    if (copyLink) {
        copyLink.addEventListener('click', function (e) {
            e.preventDefault();
            const noteLink = window.location.href;
            
            navigator.clipboard.writeText(noteLink).then(() => {
                alert('Note link copied to clipboard!');
            }).catch(err => {
                alert('Failed to copy note link.');
            });
        });
    }

    if (shareWhatsApp) {
        shareWhatsApp.addEventListener('click', function (e) {
            e.preventDefault();
            const noteLink = window.location.href;
            const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(noteLink)}`;
            window.open(whatsappUrl, '_blank');
        });
    }
});
