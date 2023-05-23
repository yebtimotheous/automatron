# import subprocess
# import pyautogui
# import time

# # Number of times to repeat the process
# num_repeats = 10

# # Number of seconds to wait between repeats
# wait_time = 1

# for i in range(num_repeats):
#     # Open Brave browser to the homepage
#     subprocess.Popen(
#         r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
#     time.sleep(wait_time)

#     for j in range(num_repeats):
#         pyautogui.press('f5')
#         time.sleep(wait_time)

#     # Close the browser
#     subprocess.call('taskkill /F /IM brave.exe')


# version 0.2.0

# # Number of times to repeat the process
# num_repeats = 10

# # Number of seconds to wait between refreshes
# refresh_time = 1

# # Number of seconds to wait between open and close the browser
# open_close_time = 1

# for i in range(num_repeats):
#     # Open Brave browser to the homepage
#     subprocess.Popen(
#         r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
#     time.sleep(open_close_time)

#     for j in range(num_repeats):
#         pyautogui.press('f5')
#         time.sleep(refresh_time)

#     # Close the browser
#     subprocess.call('taskkill /F /IM brave.exe')
#     time.sleep(open_close_time)


import subprocess
# import time

# # # Number of times to repeat the process
# # num_repeats = 10

# # # Number of seconds to wait between refreshes
# # refresh_time = 1

# # # Number of times to open and close the browser
# # open_close_repeats = 5

# # for i in range(open_close_repeats):
# #     # Open Brave browser to the homepage in the background
# #     subprocess.Popen([r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
# #                      "--start-fullscreen", "--new-window", "https://www.youtube.com/watch?v=TWh97h69b_4"])
# #     time.sleep(refresh_time)

# #     for j in range(num_repeats):
# #         subprocess.call('cmd /c "echo location.reload() | clip"', shell=True)
# #         time.sleep(refresh_time)

# #     # Close the browser
# #     subprocess.call('taskkill /F /IM brave.exe')


# # Number of times to repeat the process
# num_repeats = 10

# # Number of seconds to wait between refreshes
# refresh_time = 1

# # Number of times to open and close the browser
# open_close_repeats = 5

# for i in range(open_close_repeats):
#     # Open Brave browser to the homepage in a resized window
#     subprocess.Popen([r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
#                      "--window-size=800,600", "--new-window", "https://www.youtube.com/watch?v=TWh97h69b_4"])
#     time.sleep(refresh_time)

#     for j in range(num_repeats):
#         subprocess.call('cmd /c "echo location.reload() | clip"', shell=True)
#         time.sleep(refresh_time)

#     # Close the browser
#     subprocess.call('taskkill /F /IM brave.exe')
