import pygame
import sys
import moviepy.editor as mp

# Initialize pygame
pygame.init()

# Set screen size
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480  # Adjust based on your display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load video
video_path = "Better Call Saul.mp4"
clip = mp.VideoFileClip(video_path)

# Convert video to pygame surface
clip = clip.resize(height=SCREEN_HEIGHT)
clip.preview()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
