from PIL import ImageGrab
import time
from constants import image_name, x1, y1
from pynput.keyboard import Key, Controller
keyboard = Controller()


def get_screen(x1, y1, x2, y2):
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))


def image_to_file(image):
    image.save(image_name, "JPEG")
    return image_name


def jump(is_bird):
    if is_bird:
        keyboard.press(Key.down)
        time.sleep(0.25)
        keyboard.release(Key.down)
    else:
        keyboard.type(" ")
