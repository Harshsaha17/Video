import os

def play_video(video_name):
    try:
        # Assuming the video files are stored in the same directory as the script
        video_path = os.path.abspath(video_name)
        os.startfile(video_path)
    except Exception as e:
        print(f"Error: {e}")

play_video('harsh.mp4')