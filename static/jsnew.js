function compareProducts() {
  // Make an AJAX request to Flask route to compare products
  fetch('/hello_world', {
          method: 'POST',
          body: new FormData(document.querySelector('form'))
      })
      .then(response => response.text())
      .then(html => {
          // Update result containers with HTML content
          document.getElementById('result1').innerHTML = html;
      })
      .catch(error => console.error('Error:', error));
}
