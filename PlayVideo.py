from ffpyplayer.player import MediaPlayer
import cv2

def playVideo(file_path):
    video = cv2.VideoCapture(file_path)
    player = MediaPlayer(file_path)

    window_name = 'Video'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    paused = False  # Pause state

    while True:
        if not paused:  # Only read frames when not paused
            ret, frame = video.read()
            if not ret:
                break

            audio_frame, val = player.get_frame()

            if val != 'eof' and frame is not None:
                cv2.imshow(window_name, frame)

        
        key = cv2.waitKey(25) & 0xFF

        if key == ord('q'):  # Quit on 'q'
            break
        elif key == ord('w'):  # Toggle pause on 'w'
            paused = not paused
            player.set_pause(paused)  # Pause/resume 

    video.release()
    cv2.destroyAllWindows()

playVideo("Better-Call-Saul.mp4")