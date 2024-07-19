document.addEventListener('DOMContentLoaded', function() {
    const hamburgerContainer = document.querySelector('.hamburger-container');
    const hamburgerMenuWrapper = document.querySelector('.hamburger-menu-wrapper');


    hamburgerContainer.addEventListener('click', function() {
      hamburgerMenuWrapper.classList.toggle('active');
    });
  });
  