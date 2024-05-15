

function compareProducts() {
    // Get the values of the selected products and requirements
    var product1 = document.getElementById("select1").value;
    var product2 = document.getElementById("select2").value;
    var requirements = document.getElementById("requirements").value;

    // Perform comparison logic (example: just logging for demonstration)
    console.log("Product 1: " + product1);
    console.log("Product 2: " + product2);
    console.log("Requirements: " + requirements);

    // Display the comparison results in the respective result containers
    document.getElementById("result1-text").innerHTML = "Product 1: " + product1 + "<br>Requirements: " + requirements;
    document.getElementById("result2-text").innerHTML = "Product 2: " + product2 + "<br>Requirements: " + requirements;

    // Show the comparison result containers
    document.getElementById("result1").style.display = "block";
    document.getElementById("result2").style.display = "block";
    document.getElementById("price-btn").style.display = "block";
    /*document.getElementById("price1").style.display = "block";
    document.getElementById("price2").style.display = "block";*/
    document.getElementById("conclusion").style.display = "block";
}

function pricecomparator() {
    document.getElementById("price1").style.display = "block";
    document.getElementById("price2").style.display = "block";
    /*document.getElementById("conclusion").style.display = "block";*/
}