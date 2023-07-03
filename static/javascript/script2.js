const link2 = document.querySelector('.popup-link2');
const modal2 = document.querySelector('.popup-modal2');

link2.addEventListener('click', function(event) {
  event.preventDefault();
  modal2.style.display = 'block';
});

link2.addEventListener('blur', function() {
  modal2.style.display = 'none';
});