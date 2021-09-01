import pgzrun

GRID_WIDTH = 16
GRIGHT_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRIDTH_WIDTH * GRID_SIZE
MAP = ["WWWWWWWWWWWWWWWWWW",
       "W                W",
       "W                W",
       "W  W    KG       W",
       "W  WWWWWWWWWW    W",
       "W                W",
       "W       P        W",
       "W  WWWWWWWWWW    W",
       "W       GK  W    W",
       "W                W",
       "W                D",
       "WWWWWWWWWWWWWWWWWW",]
       
HEIGHT = GRID_HEIGHT * GRID_SIZE
def screen_coords(x, y):
  return (x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
  for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
      screen.blit("floor1", screen_coords(x, y))
      def draw():
        draw_background()

pgzrun.go()
