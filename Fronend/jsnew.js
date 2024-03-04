document.addEventListener('DOMContentLoaded', function() {
    // Get the button element
    const showButton = document.getElementById('showTextBoxes');
  
    // Get the container where text boxes will be appended
    const container = document.getElementById('textBoxContainer');
  
    // Add event listener to the button
    showButton.addEventListener('click', function() {
      // Create text boxes
      const textBox1 = document.createElement('textarea');
      const textBox2 = document.createElement('textarea');
  
      // Add any attributes or styles you want to the text boxes
      textBox1.setAttribute('placeholder', 'Enter text...');
      textBox2.setAttribute('placeholder', 'Enter more text...');
      textBox1.style.width = '300px'; // Adjust the width as needed
      textBox2.style.width = '300px'; // Adjust the width as needed
  
      // Add spacing between text boxes
      textBox1.style.marginBottom = '10px';
      textBox1.style.marginRight = '700px'; // Adjust the spacing as needed
      textBox2.style.marginBottom = '10px'; // Adjust the spacing as needed
  
      // Append text boxes to the container
      container.appendChild(textBox1);
      container.appendChild(textBox2);
  
      // Optionally, you can remove the button after it's clicked
      showButton.style.display = 'none';
    });
});
