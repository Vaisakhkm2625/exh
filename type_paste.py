
import time
from pynput import keyboard
from pynput.keyboard import Controller, Key
from copykitten import Clipboard

class ClipboardTyper:
    def __init__(self):
        self.keyboard_controller = Controller()
        self.clipboard = Clipboard()
        self.running = False

    def get_clipboard_text(self):
        """Retrieve text from the clipboard."""
        return self.clipboard.paste()

    def type_text(self, text):
        """Type text using the keyboard controller."""
        for char in text:
            if not self.running:
                break
            self.keyboard_controller.type(char)
            time.sleep(0.05)  # Adjust typing speed if necessary

    def start_typing(self):
        """Start typing clipboard content."""
        self.running = True
        clipboard_text = self.get_clipboard_text()
        if clipboard_text:
            print(f"Typing from clipboard: {clipboard_text}")
            self.type_text(clipboard_text)
        else:
            print("Clipboard is empty!")

    def stop_typing(self):
        """Stop typing."""
        self.running = False

    def run(self):
        """Start listening for keypresses."""
        def on_press(key):
            if key == Key.esc:
                print("Stopping typing...")
                self.stop_typing()
                return False  # Stop listener

        print("Press Esc to stop.")
        with keyboard.Listener(on_press=on_press) as listener:
            self.start_typing()
            listener.join()


if __name__ == "__main__":
    typer = ClipboardTyper()
    typer.run()
