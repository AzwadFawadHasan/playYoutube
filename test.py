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
    global counter
    
    if key == key.alt_l and counter %2 !=0:
        counter+=1
            
            
        
        



def on_release(key):
    global counter

    active_window = gw.getActiveWindow()
    # Get the title of the active window
    window_title = active_window.title


    print('{0} release'.format(
        key))  
    if key == key.alt_l and counter %2 ==0:
        
        counter+=1
        if "YouTube" in window_title:
            print("Word found!", window_title)
            
        time.sleep(SCREENSHOT_DELAY-.5)
        pyautogui.press('space')
        print(".............SPACE PRESSED.............")
            
        

    
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()






