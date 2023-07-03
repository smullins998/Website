const link = document.querySelector('.popup-link');
const modal = document.querySelector('.popup-modal');

link.addEventListener('click', function(event) {
  event.preventDefault();
  modal.style.display = 'block';
});

link.addEventListener('blur', function() {
  modal.style.display = 'none';
});


