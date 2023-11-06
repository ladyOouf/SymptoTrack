// # Prologue Comments
// # • Name of code artifact: script.js
// # • Description: Establishes signal between the frontend html pages and python. Inspecting html page will reveal the
// # message
// # • Programmer’s name: Sarah Martinez
// # • Data of Creation: 10.28.2023
// # • Latest Revision: 11.05.2023
// # • Brief description of each revision & author
// # • Preconditions: None
// #   Query setup: None
// # • Postconditions: None
// # • Errors: None
// # • Side effects: None
// # • Invariants: None
// # • Any known faults: None
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
