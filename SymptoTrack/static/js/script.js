async function checkSignal() {
    try {
        // Use a relative URL to make requests to the same host and port
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