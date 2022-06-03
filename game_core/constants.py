import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# set up global variables
display_width = screensize[0]
display_height = screensize[1]

# color constants
white = (255, 255, 255)
black = (0, 0, 0)
red = (0xE4,0x00,0x27)
green = (0x4F, 0xAF, 0x44)
good_health_color = green
normal_health_color = (0xff, 0x91, 0x00)
low_health_color = red
blue = (0, 0, 255)
nice_color = (0xfd, 0x30, 0xd5)
dark_green = (0x02, 0x75, 0x21)
yellow = (0xF6, 0xEB, 0x14)
dark_gray = (0x2A, 0x34, 0x92)
player_colors = [red, green, yellow,blue, nice_color, dark_gray]

# tank constants
tank_width = 40
tank_height = 12
turret_width = 3
turret_length = int(tank_width/2) + 5
wheel_width = 5
full_tank_height = tank_height + wheel_width
move_step = 3
angle_step = pi/64
initial_turret_angle = -pi/2
initial_tank_health = 100
tank_explosion_power = 40
tank_explosion_radius = 100

# simple shell constants
min_shell_speed = 12
max_shell_speed = 22
shell_speed_step = (max_shell_speed-min_shell_speed)/100
simple_shell_power = 80
simple_shell_radius = 50

# temporary simple ground
ground_height_min = 500
ground_height_max = 800
