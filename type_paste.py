
import time
from pynput import keyboard
from pynput.keyboard import Controller
import copykitten

class ClipboardTyper:
    def __init__(self):
        self.typing = False
        self.stop_typing = False
        self.keyboard_controller = Controller()

    def get_clipboard_content(self):
        """Retrieve text from the clipboard using CopyKitten."""
        try:
            return copykitten.paste()
        except Exception as e:
            print(f"Error reading clipboard: {e}")
            return ""

    def start_typing(self):
        """Start typing out the clipboard content."""
        self.typing = True
        text = self.get_clipboard_content()
        print("Starting to type clipboard content...")

        for char in text:
            if self.stop_typing:
                print("Typing stopped.")
                break
            self.keyboard_controller.type(char)
            time.sleep(0.05)  # Add a delay between keystrokes for realism

    def on_press(self, key):
        """Handle key press events."""
        if key == keyboard.Key.esc:
            self.stop_typing = True
            return False  # Stop listener

    def run(self):
        """Run the typer and listen for the stop key."""
        with keyboard.Listener(on_press=self.on_press) as listener:
            self.start_typing()
            listener.join()

# Usage
if __name__ == "__main__":
    typer = ClipboardTyper()
    typer.run()
