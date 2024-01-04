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

//Slideshow
var images = [];
var imageElements = document.querySelectorAll("#slideshow IMG");
for (var i = 1; i <= 3; i++) {
    images.push("IMG/image" + i + ".jpg");
}

var currentIndex = 0;
var slideshow = document.getElementById("slideshow");

// Function to change the image source
function changeImage() {
    slideshow.src = images[currentIndex];
    currentIndex++;
    if (currentIndex >= images.length) {
        currentIndex = 0;
    }
}

// Call the changeImage function every 3 seconds
setInterval(changeImage, 2000);