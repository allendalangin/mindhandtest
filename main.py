from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        # Bind the Android back button so the app doesn't just 'die'
        Window.bind(on_keyboard=self.on_key)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Big label to confirm the app is running
        self.label = Label(
            text="MindHand Test: OFFLINE", 
            font_size='32sp',
            color=(0, 1, 0, 1) # Green
        )
        
        # A button that does something simple
        btn = Button(
            text="Click to Test",
            size_hint=(1, 0.5),
            background_color=(0, 0.5, 1, 1)
        )
        btn.bind(on_release=self.change_text)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def change_text(self, instance):
        self.label.text = "Python is Working!"
        self.label.color = (1, 1, 0, 1) # Yellow

    def on_key(self, window, key, *args):
        # 27 is the keycode for the Android 'Back' button
        if key == 27:
            return True # Prevents app from closing instantly
        return False

if __name__ == '__main__':
    TestApp().run()
