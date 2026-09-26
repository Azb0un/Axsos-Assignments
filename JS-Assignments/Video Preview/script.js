// Grab elements once the DOM is ready
function initVideoPlayer() {
    const video = document.getElementById('myVideo');
    const container = document.querySelector('.video-container');
    const playBtn = document.getElementById('playBtn');
    const seekBar = document.getElementById('seekBar');
    const volumeIcon = document.getElementById('volumeIcon');
    const volumeBar = document.getElementById('volumeBar');
    const fullscreenBtn = document.getElementById('fullscreenBtn');

    setupPlayPause(video, playBtn);
    setupSeekBar(video, seekBar);
    setupVolumeControl(video, volumeBar, volumeIcon);
    setupFullscreen(video, container, fullscreenBtn);
}
function setupPlayPause(video, playBtn) {
    playBtn.addEventListener('click', () => togglePlay(video, playBtn));
}
function togglePlay(video, playBtn) {
    if (video.paused) {
        video.play();
        playBtn.textContent = '⏸';
    } else {
        video.pause();
        playBtn.textContent = '▶';
    }
}
function setupSeekBar(video, seekBar) {
    video.addEventListener('timeupdate', () => updateSeekBar(video, seekBar));
    seekBar.addEventListener('input', () => seekVideo(video, seekBar));
}
function updateSeekBar(video, seekBar) {
    seekBar.value = (video.currentTime / video.duration) * 100;
}
function seekVideo(video, seekBar) {
    video.currentTime = (seekBar.value / 100) * video.duration;
}
function setupVolumeControl(video, volumeBar, volumeIcon) {
    volumeBar.addEventListener('input', () => {
        setVolume(video, volumeBar);
        updateVolumeIcon(video, volumeIcon);
    });
     volumeIcon.addEventListener('click', () => toggleMute(video, volumeBar, volumeIcon));

    updateVolumeIcon(video, volumeIcon);
}

function toggleMute(video, volumeBar, volumeIcon) {
    video.muted = !video.muted;

    if (video.muted) {
        volumeBar.value = 0;
    } else {
        video.volume = video.volume === 0 ? 1 : video.volume;
        volumeBar.value = video.volume * 100;
    }
    updateVolumeIcon(video, volumeIcon);
}
function setVolume(video, volumeBar) {
    video.volume = volumeBar.value / 100;
    video.muted = video.volume === 0;
}
function updateVolumeIcon(video, volumeIcon) {
    if (video.muted || video.volume === 0) {
        volumeIcon.textContent = '🔇';
    } else if (video.volume < 0.5) {
        volumeIcon.textContent = '🔉';
    } else {
        volumeIcon.textContent = '🔊';
    }
}
function setupFullscreen(video, container, fullscreenBtn) {
    fullscreenBtn.addEventListener('click', () => toggleFullscreen(container));
}
function toggleFullscreen(container) {
    if (!document.fullscreenElement) {
        container.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
}
document.addEventListener('DOMContentLoaded', initVideoPlayer);
function isSubscribed(element){
    element.innerText="Subscribed"
}