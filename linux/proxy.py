import os
from selenium import webdriver
import time
from stem import Signal
from stem.control import Controller

# Number of times to repeat the process
num_repeats = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to open and close the browser
open_close_repeats = 5

# This script uses the Selenium webdriver to control a browser,
# the Stem library to interact with the Tor network,
# and the os library to set the path of the chrome driver.

for i in range(open_close_repeats):
    # Connect to the tor network and get a new identity (IP address)
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

    # Open Chrome browser to the youtube link with specific options:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument("--window-size=800,600")
    options.add_argument("--new-window")
    options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
    # setting path of chrome driver
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path='path/to/chromedriver')
    driver.get("https://youtu.be/3bu92rxD8YA")

    # Refresh the page for the specified number of times
    for j in range(num_repeats):
        options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
        driver.refresh()
        time.sleep(refresh_time)

    # Close the browser
    driver.quit()

# HOW TO -:
# @author: r/yebtimotheous
# This script uses the Tor network to change the IP address of the browser on each refresh.
# To use this script on Linux, Tor needs to be installed and configured on the machine.
# The following steps can be used to install and configure Tor on Ubuntu:

# 1. Add the Tor repository to your system's package manager.
    # sudo add-apt-repository ppa:webupd8team/tor-browser
# 2. Update your package manager's package list.
    # sudo apt-get update

# 3. Install Tor.
    # sudo apt-get install tor tor-browser
# 4. Start the Tor service.
    # sudo systemctl start tor

# 5. Verify that the service is running.
    # sudo systemctl status tor
# 6. Configure tor by modifying the torrc file located at /etc/tor/torrc
#    by adding the following lines: SocksPort 9050, and ControlPort 9051

# 7. Restart the tor service.
    # sudo systemctl restart tor
# 8. Replace the chrome driver path with the path to chrome driver in your linux machine and set the path for the tor browser on your machine.

# Additional features to be added in next update
# Let add add a feature for request_random_user-agent so that 
# each opened window will be from a different random user