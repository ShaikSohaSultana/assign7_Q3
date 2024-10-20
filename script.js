document.getElementById('registration-form').addEventListener('submit', function(event) {
    const userId = document.getElementById('user_id').value;
    const mobileNumber = document.getElementById('mobile_number').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    if (!userId || !mobileNumber || !password) {
        errorMessage.textContent = 'All fields are required.';
        event.preventDefault(); // Prevent form submission
    }
});
