// Prologue Comments
// • Name of code artifact: script.js
// • Description: Establishes signal between the frontend html pages and python. Inspecting html page will reveal the
// message
// • Programmer’s name: Sarah Martinez
// • Data of Creation: 10.28.2023
// • Latest Revision: 12.03.2023
// • Brief description of each revision & author
// • Preconditions: None
//   Query setup: None
// • Postconditions: None
// • Errors: None
// • Side effects: None
// • Invariants: None
// • Any known faults: revamping the entire set up the site, the script.js and jqueries are sending status codes 500 and
// # 404, regardless of what I've done, I can't remove it and it's likely due to the set up the files and the script.js

$("form[name=signup_form]").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href ="/";
    },
    error: function(resp) {
      console.log(resp);
    }
  });

  e.preventDefault();
});


// Old AJAX request code for the signup form

// if (document.getElementById('signupForm')) {
//     document.getElementById('signupForm').addEventListener('submit', function(event) {
//         event.preventDefault();
//
//         let formData = new FormData(event.target);
//         let data = Object.fromEntries(formData.entries());
//
//         fetch('/signup', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(data)
//         })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.message === 'User created successfully') {
//                     alert('Sign up successful!');
//                     window.location.href = '/';
//                 } else {
//                     alert('Error: ' + data.message);
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 alert('Something went wrong. Please try again.');
//             });
//     });
// }
//
// // AJAX request code for the login form
// if (document.getElementById('loginForm')) {
//     document.getElementById('loginForm').addEventListener('submit', function(event) {
//         event.preventDefault();
//
//         let formData = new FormData(event.target);
//         let data = Object.fromEntries(formData.entries());
//
//         fetch('/login', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(data)
//         })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.message === 'User logged in successfully') {
//                     alert('Login successful!');
//                     window.location.href = '/homepage';
//                 } else {
//                     alert('Error: ' + data.message);
//                 }
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 alert('Something went wrong. Please try again.');
//             });
//     });
// }
//
// async function checkSignal() {
//     try {
//         const response = await fetch("/");
//
//         if (response.ok) {
//             console.log('Signal received from the backend!');
//         } else {
//             console.error('Request failed with status:', response.status);
//         }
//     } catch (error) {
//         console.error('Error checking signal:', error);
//     }
// }
//
// window.addEventListener('load', checkSignal);