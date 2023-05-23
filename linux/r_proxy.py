import os
from selenium import webdriver
import time
from stem import Signal
from stem.control import Controller
import random

# Number of times to repeat the process
num_repeats = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to open and close the browser
open_close_repeats = 5

# List of user-agents to choose from
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
]

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
    # add a random user-agent for each opened window
    options.add_argument("user-agent={}".format(random.choice(user_agents)))
    driver.get("https://youtu.be/3bu92rxD8YA")

    # Refresh the page for the specified number of times
    for j in range(num_repeats):
        options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
        driver.refresh()
        time.sleep(refresh_time)

    # Close the browser
    driver.quit()
