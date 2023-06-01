import pyautogui
import time
from pynput.keyboard import Key, Listener

SCREENSHOT_DELAY = 1  # Delay between each screenshot capture
VIDEO_PLAYER_REGION = (100, 100, 500, 500)  # Region of interest on the screen
# Main program loop
previous_screenshot = None
counter=0

def on_press(key):
    print('{0} pressed'.format(
        key))
    global counter
    if key == key.alt_l and counter %2 !=0:
        print('hahahahahahalt_l released')
        #screenshot = pyautogui.screenshot(region=VIDEO_PLAYER_REGION)
        #print(screenshot)
        #if previous_screenshot is not None and screenshot != previous_screenshot:
        # Video playback has changed, take appropriate action
        # For example, simulate pressing the space bar to resume playback
        #time.sleep(0.1)
        pyautogui.keyUp('alt_l')
        counter+=1
        print(counter)
        #time.sleep(SCREENSHOT_DELAY-1)
        pyautogui.keyDown('k')
        #pyautogui.keyUp('space')
        pyautogui.keyDown('alt_l')
    
  

def on_release(key):
    global counter
    print('{0} release'.format(
        key))  
    if key == key.alt_l and counter %2 ==0:
        print('hahahahahahalt_l released')
        #screenshot = pyautogui.screenshot(region=VIDEO_PLAYER_REGION)
        #print(screenshot)
        #if previous_screenshot is not None and screenshot != previous_screenshot:
        # Video playback has changed, take appropriate action
        # For example, simulate pressing the space bar to resume playback
        
        counter+=1
        time.sleep(SCREENSHOT_DELAY-.5)
        pyautogui.press('space')
    
        #time.sleep(SCREENSHOT_DELAY)
    # if key == key.tab:
    #     #print('hahahahahahalt_l pressed')
    #     pyautogui.press('space')

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
# Constants

 



while True:
    print('ENTERED WHILE LOOP   ')
    # Capture screenshot
    screenshot = pyautogui.screenshot(region=VIDEO_PLAYER_REGION)

    # Compare current and previous screenshots
    if previous_screenshot is not None and screenshot != previous_screenshot:
        # Video playback has changed, take appropriate action
        # For example, simulate pressing the space bar to resume playback
        pyautogui.press('space')

    # Update previous screenshot
    previous_screenshot = screenshot

    # Delay before capturing the next screenshot
    time.sleep(SCREENSHOT_DELAY)





#This code can successfully pause a youtube video playing in background when alt+tab is pressed, but when alt+ tab is pressed again it cannot play the video that it paused initially