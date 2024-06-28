from setuptools import setup, find_packages

setup(
    name='video_audio_recorder',
    version='0.2.0',
    author='Shamika Likhite',
    author_email='shamilikhite@gmail.com',
    description='A package to record video and audio simultaneously',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shami09/video_audio_recorder',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pyaudio',
        'opencv-python',
        'ffmpeg-python',
    ],
)
