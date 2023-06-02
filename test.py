import pyautogui
import time
from pynput.keyboard import Key, Listener
import pygetwindow as gw




SCREENSHOT_DELAY = 1  # Delay between each screenshot capture
VIDEO_PLAYER_REGION = (100, 100, 500, 500)  # Region of interest on the screen
# Main program loop
previous_screenshot = None
counter=0

def on_press(key):
    print('{0} pressed'.format(
        key))
    
    

    
  

def on_release(key):
    global counter
    print('{0} release'.format(
        key))  
    if key == Key.alt_l and counter %2 ==0:
        print('hahahahahahalt_l released')
        counter+=1
        time.sleep(SCREENSHOT_DELAY-.5)
        # Get the active window
        active_window = gw.getActiveWindow()

        # Get the title of the active window
        window_title = active_window.title

        print("Active Window:", window_title)
        if "YouTube" in window_title:
            print("Word found!")
            pyautogui.press('space')
    
    

    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


 



# while True:
#     print('ENTERED WHILE LOOP   ')
#     # Capture screenshot
#     screenshot = pyautogui.screenshot(region=VIDEO_PLAYER_REGION)

#     # Compare current and previous screenshots
#     if previous_screenshot is not None and screenshot != previous_screenshot:
#         # Video playback has changed, take appropriate action
#         # For example, simulate pressing the space bar to resume playback
#         pyautogui.press('space')

#     # Update previous screenshot
#     previous_screenshot = screenshot

#     # Delay before capturing the next screenshot
#     time.sleep(SCREENSHOT_DELAY)





#This code can successfully pause a youtube video playing in background when alt+tab is pressed, but when alt+ tab is pressed again it cannot play the video that it paused initially