// screensharing/static/screensharing/js/screen_share.js

document.addEventListener('DOMContentLoaded', function () {
    const roomName = document.querySelector('#roomName').textContent;
    const localVideo = document.getElementById('localVideo');
    const remoteVideo = document.getElementById('remoteVideo');

    const webrtc = new SimpleWebRTC({
        localVideoEl: 'localVideo',
        remoteVideosEl: 'remoteVideo',
        autoRequestMedia: true,
        debug: false,
        detectSpeakingEvents: true,
        url: `https://api.simplewebrtc.com/v1/${roomName}`
    });

    webrtc.on('readyToCall', function () {
        webrtc.joinRoom(roomName);
    });
});
