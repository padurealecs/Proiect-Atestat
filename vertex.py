import constants
import pygame

def draw_base_line(screen):

    pygame.draw.line(screen, '#777777', (0, 50), (1200, 50), 2)

class Vertex:
    
    #creating new vertex
    def __init__(self, x, y):
        #absolute position
        self.x = x
        self.y = y

        #index used to identify the vertex in the graph
        self.index = 0

        self.grounded = False

        if self.y == 50:
            self.grounded = True


    #draws the vertex on the screen
    def draw_vertex(self, screen):
        if self.grounded:
            pygame.draw.circle(screen, '#009500', (self.x, self.y), constants.vertex_radius + 3)
        else:
            pygame.draw.circle(screen, constants.vertex_color, (self.x, self.y), constants.vertex_radius)

    def write():
        print(constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH)
    