document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("feedback-form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const fullname = document.getElementById("Fullname");
        const email = document.getElementById("email");
        const message = document.getElementById("message");
        const rating = document.getElementById("rating");
        let valid = true;

        // Validation for name, email, message, and rating fields
        // Similar to the previous example...

        if (valid) {
            // Submit the form
            const formData = new FormData();
            formData.append("fullname", fullname.value.trim());
            formData.append("email", email.value.trim());
            formData.append("message", message.value.trim());
            formData.append("rating", rating.value);

            // Here, you can send formData to your server using AJAX or fetch
            // Example:
            // fetch("submit_feedback.php", {
            //     method: "POST",
            //     body: formData
            // })
            // .then(response => {
            //     if (response.ok) {
            //         // Display success message or redirect
            //     } else {
            //         throw new Error("Network response was not ok.");
            //     }
            // })
            // .catch(error => {
            //     // Handle error
            // });

            // For demonstration purposes, you can log the form data to the console
            console.log("Form data:", Object.fromEntries(formData.entries()));
        }
    });

    // Form validation functions...
});
