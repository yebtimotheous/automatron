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

# setting path of chrome driver
# os.environ["webdriver.chrome.driver"] = "C:\Users\YebTimotheous\Downloads\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = r"C:\Users\YebTimotheous\Downloads\chromedriver_win32\chromedriver.exe"

for i in range(open_close_repeats):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

    # Open Brave browser to the homepage in a resized window
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument("--window-size=800,600")
    options.add_argument("--new-window")
    options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://youtu.be/3bu92rxD8YA")

    for j in range(num_repeats):
        options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
        driver.refresh()
        time.sleep(refresh_time)

    # Close the browser
    driver.quit()
