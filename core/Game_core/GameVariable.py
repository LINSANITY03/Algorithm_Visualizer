SCREEN_WIDTH = 720
SCREEN_HEIGHT = 405
DIMENSIONS = 11  # representing 11x11 board
SQ_SIZE = SCREEN_HEIGHT // DIMENSIONS
MAX_FPS = 30
IMAGES = {}

# Rectangle dimensions
RECT_WIDTH = RECT_HEIGHT = SQ_SIZE * DIMENSIONS

# Calculate the position of the rectangle to center it
RECT_X = (SCREEN_WIDTH - RECT_WIDTH) // 2
RECT_Y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2
