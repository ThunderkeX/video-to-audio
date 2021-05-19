import imageio
imageio.plugins.ffmpeg

import moviepy.editor
# Replace the parameter with the location of the video
video = moviepy.editor.VideoFileClip(r"C:\Users\se\Pictures\a.mov")  # Entering the videofile

audio = video.audio

# Replace the parameter with the location along with filename
audio.write_audiofile(r"C:\Users\se\Pictures\a.mp3")

print('converted successfully')