const link5 = document.querySelector('.popup-link5');
const modal5 = document.querySelector('.popup-modal5');

link5.addEventListener('click', function(event) {
  event.preventDefault();
  modal5.style.display = 'block';
});

link5.addEventListener('blur', function() {
  modal5.style.display = 'none';
});