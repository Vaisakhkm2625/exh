from pynput import mouse
from PIL import ImageGrab
import threading

# Global variables to store the coordinates
start_x = start_y = end_x = end_y = None

def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y
    if pressed:
        # Record the start position when mouse is pressed
        start_x, start_y = x, y
    else:
        # Record the end position when mouse is released
        end_x, end_y = x, y
        # Stop listener once the mouse is released
        return False

def crop_screenshot(img, start_x, start_y, end_x, end_y):
    # Normalize coordinates (make sure start is top-left, end is bottom-right)
    left = min(start_x, end_x)
    top = min(start_y, end_y)
    right = max(start_x, end_x)
    bottom = max(start_y, end_y)
    
    # Crop the image using the specified coordinates
    cropped_img = img.crop((left, top, right, bottom))
    return cropped_img

def take_and_crop_screenshot(image_file_path):
    # Take a full-screen screenshot
    full_screenshot = ImageGrab.grab()

    # Collect mouse events until released
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Once mouse listener is done, crop the screenshot
    if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
        cropped_img = crop_screenshot(full_screenshot, start_x, start_y, end_x, end_y)
        cropped_img.save(image_file_path)
    else:
        print("No area selected.")

def take_and_crop_screenshot_thread(image_file_path):
    print("Taking screenshot...")
    screenshot_thread = threading.Thread(target=take_and_crop_screenshot, args=(image_file_path,))
    screenshot_thread.start()

if __name__ == "__main__":
    # This function can be triggered to start screenshot capturing
    print("Ready to take a screenshot. Click and drag to select an area.")
    take_and_crop_screenshot_thread('./screenshot.png')
