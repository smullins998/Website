document.addEventListener('DOMContentLoaded', function() {
  var codeHover = document.querySelector('.code-hover');
  var codeModal = document.querySelector('#codeModal');

  codeHover.addEventListener('mouseover', function() {
    codeModal.style.display = 'block';
  });

  codeHover.addEventListener('mouseout', function() {
    codeModal.style.display = 'none';
  });
});