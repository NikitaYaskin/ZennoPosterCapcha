import pyautogui
import time
import datetime
import logging
import os

# 1. OPTIMIZATION: Let the logging module handle timestamps automatically.
logging.basicConfig(
    filename='captcha.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S'
)

def load_images(img_dir="img"):
    """Loads images and automatically separates digit files from the title."""
    data = {}
    digits = []
    
    # Ensure directories exist so pyautogui.screenshot doesn't crash
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs('failed_captcha', exist_ok=True)
    os.makedirs('success', exist_ok=True)

    for filename in os.listdir(img_dir):
        name, _ = os.path.splitext(filename) # Splits '1.png' into '1' and '.png'
        path = os.path.join(img_dir, filename)
        
        if name.isdigit():
            key = int(name)
            data[key] = path
            digits.append(key)
        else:
            data[name] = path # Handles 'title.png' automatically
            
    logging.info(f'Loaded images from folder: {list(data.values())}')
    return data, sorted(digits)

# Initialize data and variables
data, digits_on_screen = load_images()
num_captchas = 0

window_location = (670, 380, 330, 270) 
digit_location = (691, 457, 300, 146) 
enter_button = (828, 621) 

logging.info('Downloading the program / Starting script')

def save_failed_captcha(info_keys):
    """Saves a screenshot with a unique timestamp to prevent overwriting."""
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    filename = f'failed_captcha/failed_{info_keys}_{timestamp}.png'
    pyautogui.screenshot(filename, region=window_location)
    logging.warning(f'Captcha failed or not entered. Digits found: {info_keys}')

while True:
    # 2. OPTIMIZATION: Use .get() to prevent KeyErrors if 'title' is missing
    if pyautogui.locateOnScreen(data.get('title'), region=window_location, grayscale=True):
        info = {}
        
        for digit in digits_on_screen:
            # 3. OPTIMIZATION: Only search the screen once per digit
            center = pyautogui.locateCenterOnScreen(data[digit], region=digit_location, grayscale=True)
            if center:
                info[digit] = center
                logging.info(f'Number {digit} found at {center}')

        # 4. OPTIMIZATION: Cleaned up conditional logic
        # Assuming exactly 4 digits are required to solve the CAPTCHA based on your original logic
        if len(info) != 4:
            pyautogui.alert(f'Incorrect number of digits found: {list(info.keys())}')
            save_failed_captcha(list(info.keys()))
            continue 

        # Extract sorted keys to draw the lines in numerical order
        sorted_keys = sorted(info.keys())
        first_point = info[sorted_keys[0]]

        # Move to the first digit and hold the mouse down
        pyautogui.moveTo(first_point.x, first_point.y)
        pyautogui.mouseDown()
        logging.info('Left mouse button pressed')

        # Drag through all points
        for key in sorted_keys:
            pyautogui.moveTo(x=info[key].x, y=info[key].y)
            logging.info(f'Cursor moved to point {key}')

        pyautogui.mouseUp()
        logging.info('Left mouse button released')

        # Save success screenshot
        timestamp = datetime.datetime.now().strftime("%H%M%S")
        success_file = f'success/success_{timestamp}_{list(info.keys())}.png'
        pyautogui.screenshot(success_file, region=window_location)
        logging.info('Success screenshot taken')

        pyautogui.click(enter_button)
        logging.info('Pressed Enter')
        time.sleep(1)

        # Verify if the CAPTCHA was actually solved
        if pyautogui.locateOnScreen(data.get('title'), region=window_location, grayscale=True):
            save_failed_captcha(list(info.keys()))
            continue
        else:
            num_captchas += 1
            logging.info(f'Entered {num_captchas} captchas successfully.')
            time.sleep(30)
