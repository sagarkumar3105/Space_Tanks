import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# set up global variables
display_width = screensize[0]
display_height = screensize[1]
