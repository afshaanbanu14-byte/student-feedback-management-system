// Registration
const registerForm = document.querySelector("#registerForm");

if (registerForm) {
    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const name = registerForm.querySelector('input[placeholder="Enter your full name"]').value;
        const email = registerForm.querySelector('input[placeholder="Enter your email"]').value;
        const password = registerForm.querySelector('input[placeholder="Create a password"]').value;
        const department = registerForm.querySelector('input[placeholder="Enter your department"]').value;
        const year = registerForm.querySelector("select").value;

        if (name === "" || email === "" || password === "" || department === "" || year === "Select your year") {
            alert("Please fill in all the fields.");
            return;
        }

        alert("Registration successful!");
    });
}


// Login
const loginForm = document.querySelector("#loginForm");

if (loginForm) {
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const email = document.querySelector("#loginEmail").value;
        const password = document.querySelector("#loginPassword").value;

        if (email === "" || password === "") {
            alert("Please enter your email and password.");
            return;
        }

        alert("Login successful!");
    });
}


// Feedback
function submitFeedback(event) {
    event.preventDefault();

    const name = document.getElementById("studentName").value.trim();
    const subject = document.getElementById("subject").value.trim();
    const rating = document.getElementById("rating").value;
    const comments = document.getElementById("comments").value.trim();

    if (name === "" || subject === "" || rating === "" || comments === "") {
        alert("Please fill in all fields.");
        return;
    }

    alert("Thank you! Your feedback has been submitted successfully.");

    document.getElementById("feedbackForm").reset();
}