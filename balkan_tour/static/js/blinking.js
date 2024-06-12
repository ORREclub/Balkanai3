<!--neatsimenu tiksliai ka tas Domcontent daro, bet tipo pagreitina skripta-->
document.addEventListener('DOMContentLoaded', function() {
    const header = document.getElementById('blinking-header');
    setInterval(() => {
        header.classList.toggle('blink');
    }, 5000);
});
