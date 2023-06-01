# import keyboard as k
# import time

# # Global variables
# previous_window = None

# def on_tab_change(e):
#     global previous_window

#     # Get the active window
#     current_window = k.get_active_window()

#     # Compare current and previous windows
#     if current_window != previous_window:
#         # Tab has changed, take appropriate action
#         print("YouTube tab changed!")

#     # Update previous window
#     previous_window = current_window

# # Keep the program running
# while True:
#     if k.is_pressed('alt') and k.is_pressed('tab'):
#         on_tab_change(None)
#         time.sleep(0.2)  # Delay to avoid repeated detection
#     time.sleep(0.1)

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == key.alt_l:
        print('hahahahahahalt_l released')
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()