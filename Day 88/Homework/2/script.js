const images = [
    'image.png',
    'image1.png',
    'image2.png'
];

let currentIndex = 0;

const imageElement = document.getElementById('carousel-image');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

function updateImage() {
    imageElement.src = images[currentIndex];
}

prevButton.addEventListener('click', () => {
    if (currentIndex < images.length - 1)  {
        currentIndex--;

    } else {
        currentIndex = 0;
    }
    updateImage();
});

nextButton.addEventListener('click', () => {
    if (currentIndex < images.length + 1)  {
        currentIndex++;

    } else {
        currentIndex = 0;
    }
    updateImage();
});