const link4 = document.querySelector('.popup-link4');
const modal4 = document.querySelector('.popup-modal4');

link4.addEventListener('click', function(event) {
  event.preventDefault();
  modal4.style.display = 'block';
});

link4.addEventListener('blur', function() {
  modal4.style.display = 'none';
});