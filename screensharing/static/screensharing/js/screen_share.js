// screensharing/static/screensharing/js/screen_share.js

document.addEventListener('DOMContentLoaded', function () {
    const roomNameElement = document.querySelector('#roomName');
    console.log(roomNameElement); 
    const roomName = roomNameElement ? roomNameElement.textContent : 'room';
    

    const webrtc = new SimpleWebRTC({
        localVideoEl: '',
        remoteVideosEl: '',
        autoRequestMedia: true,
        debug: false,
        detectSpeakingEvents: true,
        url: `https://api.simplewebrtc.com/v1/${roomName}`
    });

    webrtc.on('readyToCall', function () {
        // Join the room and start sharing the screen
        webrtc.joinRoom(roomName);
        webrtc.shareScreen();
    });
});
