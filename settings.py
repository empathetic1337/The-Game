import math
import sqlite3


# game settings
with open('resources/database/user.txt', 'r') as file:
    user = file.read()
conn = sqlite3.connect("resources/database/users.db")
cur = conn.cursor()
res = cur.execute('SELECT width FROM users WHERE name = ?', (user,)).fetchone()
res1 = cur.execute('SELECT height FROM users WHERE name = ?', (user,)).fetchone()
WIDTH = res[0]
HEIGHT = res1[0]
RES = WIDTH, HEIGHT
if WIDTH == 1920:
    scaler = 1.1
elif WIDTH == 1600:
    scaler = 0.8
else:
    scaler = 0.7
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
conn = sqlite3.connect("resources/database/users.db")
cur = conn.cursor()
res3 = cur.execute('SELECT fpslock FROM users WHERE name = ?', (user,)).fetchone()
FPS = res3[0]

PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.004
PLAYER_SIZE_SCALE = 100
PLAYER_MAX_HEALTH = 100

conn = sqlite3.connect("resources/database/users.db")
cur = conn.cursor()
res2 = cur.execute('SELECT sensitivity FROM users WHERE name = ?', (user,)).fetchone()
MOUSE_SENSITIVITY = float(res2[0])
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_TOP = 100
MOUSE_BORDER_BOTTOM = HEIGHT - MOUSE_BORDER_TOP

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
