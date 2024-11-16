import copykitten
import keyboard
import time

# Global flag to control typing
is_typing = True

def stop_typing(event):
    """Stop typing when Esc is pressed."""
    global is_typing
    is_typing = False

def type_clipboard_content():
    global is_typing
    # Get text from the clipboard
    text = copykitten.paste()
    
    # Iterate through each character and type it out
    for char in text:
        if not is_typing:
            print("Typing stopped.")
            break
        if char.isupper():  # If the character is uppercase
            keyboard.press('shift')
            keyboard.write(char.lower())  # Write the lowercase equivalent while holding shift
            keyboard.release('shift')
        elif char in "~!@#$%^&*()_+{}|:\"<>?":
            # Handle special characters that require the Shift key
            shift_mappings = {
                '~': '`', '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7',
                '*': '8', '(': '9', ')': '0', '_': '-', '+': '=', '{': '[', '}': ']', '|': '\\',
                ':': ';', '"': "'", '<': ',', '>': '.', '?': '/'
            }
            keyboard.press('shift')
            keyboard.write(shift_mappings[char])
            keyboard.release('shift')
        else:
            # Type the character directly
            keyboard.write(char)
        time.sleep(0.05)  # Optional: Add a delay between key presses for natural typing effect

if __name__ == "__main__":
    # Add a hook to listen for the Esc key
    keyboard.on_press_key('esc', stop_typing)
    
    print("Typing clipboard content. Press 'Esc' to stop.")
    type_clipboard_content()
    
    # Remove the hook to clean up
    keyboard.unhook_all()
