// screensharing/static/screensharing/js/main.js

document.addEventListener('DOMContentLoaded', function () {
    const startButton = document.getElementById('startButton');

    startButton.addEventListener('click', async function () {
        // Request a session ID from the backend
        const response = await fetch('/generate_session/');
        const data = await response.json();

        // Initialize simplewebrtc with the session ID
        const webrtc = new SimpleWebRTC({
            localVideoEl: '',
            remoteVideosEl: '',
            autoRequestMedia: true,
            url: `https://api.simplewebrtc.com/v1/${data.session_id}`
        });

        // Start screen sharing
        webrtc.shareScreen();
    });
});
