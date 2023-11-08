# pip install moviepy
import moviepy.editor

# read video file
video = moviepy.editor.videofileclip('videoName.mp4')

# convert video data to audio
audio = video.audio

# save audio file
audio.write_audiofile('audioName.mp3')