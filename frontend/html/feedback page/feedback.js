ocument.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("feedback-form");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const fullname = document.getElementById("Fullname");
        const email = document.getElementById("email");
        const message = document.getElementById("message");
        let valid = true;

        if (fullname.value.trim() === "") {
            valid = false;
            displayErrorMessage(fullname, "Please enter your name.");
        } else {
            removeErrorMessage(fullname);
        }

        if (email.value.trim() === "") {
            valid = false;
            displayErrorMessage(email, "Please enter your email address.");
        } else if (!isValidEmail(email.value.trim())) {
            valid = false;
            displayErrorMessage(email, "Please enter a valid email address.");
        } else {
            removeErrorMessage(email);
        }

        if (message.value.trim() === "") {
            valid = false;
            displayErrorMessage(message, "Please enter your message.");
        } else {
            removeErrorMessage(message);
        }

        if (valid) {
            // Submit the form
            form.submit();
        }
    });

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function displayErrorMessage(field, message) {
        const errorMessage = document.createElement("div");
        errorMessage.classList.add("error-message");
        errorMessage.textContent = message;
        field.parentNode.insertBefore(errorMessage, field.nextSibling);
    }

    function removeErrorMessage(field) {
        const errorMessage = field.parentNode.querySelector(".error-message");
        if (errorMessage) {
            errorMessage.remove();
        }
    }
});