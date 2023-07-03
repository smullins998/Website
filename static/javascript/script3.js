const link3 = document.querySelector('.popup-link3');
const modal3 = document.querySelector('.popup-modal3');

link3.addEventListener('click', function(event) {
  event.preventDefault();
  modal3.style.display = 'block';
});

link3.addEventListener('blur', function() {
  modal3.style.display = 'none';
});