import os
from selenium import webdriver
import time
from stem import Signal
from stem.control import Controller
from requests_random_user_agent import RandomUserAgent
import random

# Number of times to repeat the process
num_repeats = 10

# Number of seconds to wait between refreshes
refresh_time = 1

# Number of times to open and close the browser
open_close_repeats = 5

# Instantiate RandomUserAgent
user_agent = RandomUserAgent()

# List of proxies or VPNs to use
proxies = ["proxy1:port", "proxy2:port", "proxy3:port"]

# setting path of chrome driver
os.environ["webdriver.chrome.driver"] = r"path/to/chromedriver"

# No user-agent
# for i in range(open_close_repeats):
#     # Open Brave browser to the homepage in a resized window
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-fullscreen")
#     options.add_argument("--window-size=800,600")
#     options.add_argument("--new-window")
#     # Choose a random proxy from the list
#     proxy = random.choice(proxies)
#     options.add_argument(f"--proxy-server={proxy}")
#     driver = webdriver.Chrome(chrome_options=options,
#                               executable_path='path/to/chromedriver')
#     driver.get("https://example.com")
#     for j in range(num_repeats):
#         driver.refresh()
#         time.sleep(refresh_time)
#     # Close the browser
#     driver.quit()

# Added support for user-agent
for i in range(open_close_repeats):
    # Open Brave browser to the homepage in a resized window
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument("--window-size=800,600")
    options.add_argument("--new-window")
    # Choose a random proxy from the list
    proxy = random.choice(proxies)
    options.add_argument(f"--proxy-server={proxy}")
    # Set a random user agent
    options.add_argument(f"--user-agent={user_agent.get()}")
    driver = webdriver.Chrome(chrome_options=options,
                              executable_path='path/to/chromedriver')
    driver.get("https://example.com")
    for j in range(num_repeats):
        driver.refresh()
        time.sleep(refresh_time)
    # Close the browser
    driver.quit()
