function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function addToCart() {
    // Get the form element
    var form = document.getElementById("add-to-cart-form");

    // Get the form action URL
    var url = form.getAttribute("action");

    // Get the form data
    var formData = new FormData(form);

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure the XMLHttpRequest object
    xhr.open("POST", url, true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

    // Define the onload callback function
    xhr.onload = function() {
        // Check if the request was successful
        if (xhr.status >= 200 && xhr.status < 300) {
            // Do something with the response, if needed
            console.log("Item added to cart successfully!");
        } else {
            // Handle the error, if any
            console.error("Error adding item to cart:", xhr.statusText);
        }
    };

    // Send the form data
    xhr.send(formData);
}
