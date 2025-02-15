document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictionForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch("/predict/", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").textContent = "Predicted Insurance Cost: $" + data.prediction.toFixed(2);
        })
        .catch(error => console.error("Error:", error));
    });
});
