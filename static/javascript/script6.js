const link6 = document.querySelector('.popup-link6');
const modal6 = document.querySelector('.popup-modal6');

link6.addEventListener('click', function(event) {
  event.preventDefault();
  modal6.style.display = 'block';
});

link6.addEventListener('blur', function() {
  modal6.style.display = 'none';
});