from ffpyplayer.player import MediaPlayer
import cv2

def playVideo(file_path):
    video = cv2.VideoCapture(file_path)
    player = MediaPlayer(file_path)

    window_name = 'Video'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        audio_frame, val = player.get_frame()

        if val != 'eof' and frame is not None:
            cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

playVideo('Better-Call-Saul.mp4')