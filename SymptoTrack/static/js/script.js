// Prologue Comments
// • Name of code artifact: script.js
// • Description: Establishes signal between the frontend html pages and python. Inspecting html page will reveal the
// message
// • Programmer’s name: Sarah Martinez
// • Data of Creation: 10.28.2023
// • Latest Revision: 11.19.2023
// • Brief description of each revision & author
// • Preconditions: None
//   Query setup: None
// • Postconditions: None
// • Errors: None
// • Side effects: None
// • Invariants: None
// • Any known faults: loginForm currently is catching an error and returning 'Something went wrong', which does not
// allow me to login. Likely linked to the python code and possible index.html



// AJAX request code for the signup form

if (document.getElementById('signupForm')) {
    document.getElementById('signupForm').addEventListener('submit', function(event) {
        event.preventDefault();

        let formData = new FormData(event.target);
        let data = Object.fromEntries(formData.entries());

        fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.message === 'User created successfully') {
                    alert('Sign up successful!');
                    window.location.href = '/';
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
    });
}

// AJAX request code for the login form
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();

        let formData = new FormData(event.target);
        let data = Object.fromEntries(formData.entries());

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.message === 'User logged in successfully') {
                    alert('Login successful!');
                    window.location.href = '/homepage';
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
            });
    });
}

async function checkSignal() {
    try {
        const response = await fetch("/");

        if (response.ok) {
            console.log('Signal received from the backend!');
        } else {
            console.error('Request failed with status:', response.status);
        }
    } catch (error) {
        console.error('Error checking signal:', error);
    }
}

window.addEventListener('load', checkSignal);