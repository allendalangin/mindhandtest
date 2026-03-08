import os
import time

# --- CRITICAL FIXES FOR WINDOWS & OBS ---
# Force Kivy to use OpenCV
os.environ['KIVY_CAMERA'] = 'opencv'
# Use DirectShow (DSHOW) as it handles OBS Virtual Camera better than MSMF
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
os.environ["OPENCV_VIDEOIO_PRIORITY_DSHOW"] = "1"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.core.window import Window
import cv2

# Set window size for a mobile-like feel
Window.size = (400, 700)

class MindHandCamera(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # --- AUTO-DETECT WORKING CAMERA INDEX ---
        # OBS often hijacks index 0. We'll search for the first real feed.
        working_index = -1
        for i in range(5): # Check first 5 indices
            cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    working_index = i
                    cap.release()
                    break
            cap.release()

        if working_index == -1:
            print("❌ No working camera found! Ensure OBS Virtual Camera is STARTED or webcam is plugged in.")
            working_index = 0 # Fallback

        print(f"✅ Using Camera Index: {working_index}")

        # 1. Camera Preview
        self.camera = Camera(play=True, resolution=(640, 480), index=working_index)
        self.layout.add_widget(self.camera)

        # 2. Control Buttons
        self.controls = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing=10)

        self.play_button = ToggleButton(text='Stop Camera', state='down')
        self.play_button.bind(on_press=self.toggle_camera)
        
        self.capture_button = Button(text='Capture & Save', background_color=(0.2, 0.8, 0.2, 1))
        self.capture_button.bind(on_press=self.capture_image)

        self.controls.add_widget(self.play_button)
        self.controls.add_widget(self.capture_button)
        self.layout.add_widget(self.controls)

        return self.layout

    def toggle_camera(self, *args):
        self.camera.play = (self.play_button.state == 'down')
        self.play_button.text = 'Stop Camera' if self.camera.play else 'Start Camera'

    def capture_image(self, *args):
        timestr = time.strftime("%Y%m%d_%H%M%S")
        filename = f"MindHand_{timestr}.png"
        self.camera.export_to_png(filename)
        print(f"📸 Image saved as: {filename}")

if __name__ == '__main__':
    MindHandCamera().run()
