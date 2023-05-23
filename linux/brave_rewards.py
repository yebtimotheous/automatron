import subprocess
import time

# Number of times to repeat the process
num_repeats = 10

# Number of seconds to wait between refreshes
refresh_time = 2

# Number of times to open and close the browser
open_close_repeats = 5

# Main loop that runs for the specified number of times
for i in range(open_close_repeats):
    # Open Brave browser to the homepage
    subprocess.Popen(['brave-browser'])
    time.sleep(refresh_time)

    # Loop that refreshes the page for the specified number of times
    for j in range(num_repeats):
        subprocess.call(['xdotool', 'key', 'F5'])
        time.sleep(refresh_time)

    # Close the browser
    subprocess.call(['pkill', 'brave-browser'])
