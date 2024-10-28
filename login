<!-- Yousuf Ismail (YXI220002)-->


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flash Feed - Sign In</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main container that centers the login form on the page -->
    <div class="login-container">
        <!-- Header containing the site's name -->
        <header>
            <h1>Flash Feed</h1>
        </header>
        <!-- Form for user login -->
        <form id="loginForm">
            <h2>Sign in</h2>
            <!-- Username input group -->
            <div class="input-group">
                <input type="text" id="username" placeholder="Username" required>
            </div>
            <!-- Password input group -->
            <div class="input-group">
                <input type="password" id="password" placeholder="Password" required>
            </div>
            <!-- Links for user actions like account creation and password recovery -->
            <div class="links">
                <a href="#">Don't have an account?</a>
                <a href="#">Forgot Password?</a>
                <a href="#">Forgot Username?</a>
            </div>
            <!-- Submit button for the form -->
            <button type="submit">Sign in</button>
        </form>
    </div>
    <script src="script.js"></script>
</body>
</html>




/* Base styles for the entire document, setting font and background */
body, html {
    height: 100%;
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Styles for the main login container, centering it and adding aesthetics */
.login-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    background: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    border-radius: 8px;
    text-align: center;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
}

/* Styling for the header within the login container */
header h1 {
    color: gray;
    margin: 0;
    font-size: 1.5em;
}

/* Styling for the form heading */
form h2 {
    margin: 20px 0;
}

/* Margin for input groups to space them out */
.input-group {
    margin-bottom: 20px;
}

/* Styles for text and password inputs, setting size and border */
input[type="text"],
input[type="password"] {
    width: 95%;  /* Adjusted to slightly less than full width to fit better within the container */
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Styles for the button, including hover effects */
button {
    width: 100%;
    padding: 10px;
    border: none;
    background-color: #007BFF;
    color: white;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

/* Styles for the additional action links under the form */
.links a {
    display: inline-block;
    margin: 10px 5px;
    color: #007BFF;
    text-decoration: none;
}

.links a:hover {
    text-decoration: underline;
}


// script.js
// This script handles the client-side behavior of the login form.
// Currently, it prevents the default form submission and logs the input values.
// Future implementation will include AJAX calls to validate credentials against a database.
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    console.log('Username:', username, 'Password:', password);
    // Placeholder for AJAX call for credential validation once backend is implemented
});



