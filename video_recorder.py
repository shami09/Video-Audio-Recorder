import cv2
import threading

class VideoRecorder:
    def __init__(self, filename='my_video.mp4', capture_device_index=0, width=640, height=480, fps=30):
        self.filename = filename
        self.capture_device_index = capture_device_index
        self.width = width
        self.height = height
        self.fps = fps

        self.video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
        self.video_capture = cv2.VideoCapture(capture_device_index)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.recording = False
        self.video_thread = threading.Thread(target=self.record_video)

    def start_recording(self):
        self.recording = True
        self.video_thread.start()

    def stop_recording(self):
        self.recording = False
        self.video_thread.join()

    def record_video(self):
        while self.recording:
            ret, frame = self.video_capture.read()
            if not ret:
                break
            self.video_writer.write(frame)

        self.video_capture.release()
        self.video_writer.release()
