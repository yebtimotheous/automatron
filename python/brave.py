import subprocess
import pyautogui
import time

# version 0.2.1

# Number of times to repeat the process
num_repeats = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to open and close the browser
open_close_repeats = 5

for i in range(open_close_repeats):
    # Open Brave browser to the homepage
    subprocess.Popen(
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
    time.sleep(refresh_time)

    for j in range(num_repeats):
        pyautogui.press('f5')
        time.sleep(refresh_time)

    # Close the browser
    subprocess.call('taskkill /F /IM brave.exe')
