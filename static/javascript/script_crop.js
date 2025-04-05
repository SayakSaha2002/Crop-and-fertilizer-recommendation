document.getElementById("cropForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Collect form data
    const soilColor = document.getElementById("soil_color").value;
    const n = document.getElementById("n").value;
    const p = document.getElementById("p").value;
    const k = document.getElementById("k").value;
    const ph = document.getElementById("ph").value;
    const rainfall = document.getElementById("rainfall").value;
    const temperature = document.getElementById("temperature").value;

    // Send form data to the server
    fetch('/crop', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            soil_color: soilColor,
            n: n,
            p: p,
            k: k,
            ph: ph,
            rainfall: rainfall,
            temperature: temperature
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update the popup message with the server's response
        document.getElementById("popupText").textContent = data.prediction_text;

        // Display the crop image in the popup if it exists
        const popupImage = document.getElementById("popupImage");
        if (data.crop_image) {
            popupImage.src = data.crop_image;
            popupImage.style.display = 'block';  // Show the image
        } else {
            popupImage.style.display = 'none';  // Hide the image if no crop is predicted
        }

        // Display the popup and overlay
        document.getElementById("popupMessage").style.display = "block";
        document.getElementById("overlay").style.display = "block";
    })
    .catch(error => console.error("Error:", error));
});

function closePopup() {
    document.getElementById("popupMessage").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
