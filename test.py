from moviepy.editor import VideoFileClip

# Load your video
video = VideoFileClip('Better-Call-Saul.mp4')

# Resize the video
resized_video = video.resize(height=480)  # Resize to 480px height, keeping aspect ratio

# Write the result to a new file
resized_video.write_videofile('resized_video.mp4')
