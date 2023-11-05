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
