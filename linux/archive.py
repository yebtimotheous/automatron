import subprocess
import time

# Number of windows to open
num_windows = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to open and close the browser
open_close_repeats = 5

for i in range(open_close_repeats):
    for j in range(num_windows):
        # Open Brave browser to the homepage
        subprocess.Popen(['brave-browser', '--new-window',
                         '--window-size=800,600', 'https://brave.com'])
        time.sleep(refresh_time)
    time.sleep(refresh_time*5)
    # Close all open Brave browser windows
    subprocess.call(['pkill', 'brave-browser'])


# update verson with refresh time

# Number of windows to open
num_windows = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to refresh the page before closing and reopening the window
num_repeats = 5

# Number of times to open and close the browser
open_close_repeats = 5

for i in range(open_close_repeats):
    for j in range(num_windows):
        # Open Brave browser to the homepage
        subprocess.Popen(['brave-browser', '--new-window',
                         '--window-size=800,600', 'https://brave.com'])
        time.sleep(refresh_time)
        for k in range(num_repeats):
            subprocess.call(['xdotool', 'key', 'F5'])
            time.sleep(refresh_time)
    time.sleep(refresh_time*5)
    # Close all open Brave browser windows
    subprocess.call(['pkill', 'brave-browser'])
