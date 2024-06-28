### Video Audio Recorder: Recording Audio and Video on the device simultaneously using device microphone and camera module/ device camera

Features
* Record audio and video simultaneously
* Use device's built-in microphone and camera
* Save recordings in common formats
* Easy-to-use interface

Note: This package is in beta testing.

### Installation and usage
# Steps to Install video-audio-recorder

1. **(Optional but Highly Recommended) Create a virtual environment with Python (version > 3.10). If you are using conda, run the following on terminal:**
    ```bash
    conda create -n <env name> python=3.9
    conda activate <env name>
    ```

2. **On terminal, install video-audio-recorder by:**
    ```bash
    pip install video-audio-recorder
    ```

3. **Once done, the application can be launched in a Jupyter notebook session via:**
    ```python
    from video_audio_recorder.recorder import record_video_and_audio
    record_video_and_audio(video_path='my_video.mp4', audio_path='output_audio.wav', output_path='merged_video.mp4', record_time=10)
    ```
    where output_path is the folder where you want to store the recording in .mp4 format. This will record video for 10 sec.

