import ffmpeg
import time
from .video_recorder import VideoRecorder
from .audio_recorder import AudioRecorder

def record_video_and_audio(video_path='my_video.mp4', audio_path='output_audio.wav', output_path='merged_video_new.mp4', record_time=10):
    video_recorder = VideoRecorder(filename=video_path)
    audio_recorder = AudioRecorder(filename=audio_path)

    audio_recorder.start_recording()
    video_recorder.start_recording()

    time.sleep(record_time)

    video_recorder.stop_recording()
    audio_recorder.stop_recording()

    temp_audio_path = 'temp_audio.aac'

    # Convert audio to AAC format
    ffmpeg.input(audio_path).output(temp_audio_path, acodec='aac').run()

    # Merge video and converted audio
    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(temp_audio_path)
    out = ffmpeg.output(video, audio, output_path, vcodec='copy', acodec='copy', strict='experimental')
    out.run()
