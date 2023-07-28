// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

// Select all alert close buttons
let alertCloseButtons = document.querySelectorAll('.alert__close');

// Add click event listener to each alert close button
alertCloseButtons.forEach(button => {
  button.addEventListener('click', function() {
    // Find the parent alert element and hide it when the close button is clicked
    let alertWrapper = this.closest('.alert');
    if (alertWrapper) {
      alertWrapper.style.display = 'none';
    }
  });
});
