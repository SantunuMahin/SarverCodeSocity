
document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent default form submission
    let formValid = validateForm();
    if (formValid) {
        document.getElementById('submitBtn').disabled = true; // Disable submit button
        document.getElementById('loader').style.display = 'block'; // Show loader
        this.submit(); // Proceed with form submission
    }
});

function validateForm() {
    const fields = document.querySelectorAll('input[type="text"], input[type="email"]');
    let valid = true;

    fields.forEach(field => {
        if (!field.value.trim()) {
            field.style.border = '2px solid red'; // Highlight invalid fields
            valid = false;
        } else {
            field.style.border = ''; // Remove red border if field is valid
        }
    });

    return valid;
}
