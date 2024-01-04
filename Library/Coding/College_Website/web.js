 // Read content from body.txt using JavaScript
            fetch('body.txt')
                .then(response => response.text())
                .then(content => {
                    document.getElementById('content').innerHTML = content;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
                
 // JavaScript code here
            const buttons = document.querySelectorAll('.button');
            
            buttons.forEach(button => {
                button.addEventListener('click', () => {
                    alert('This is a premium feature. Please upgrade to access.');
                });
            });


function changeImage() {
    slideshow.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeImage, 1500);
