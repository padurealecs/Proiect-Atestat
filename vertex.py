import constants
import pygame

def draw_base_line(screen):

    pygame.draw.line(screen, '#777777', (0, constants.SCREEN_HEIGHT - 50), (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT - 50), 2)

class Vertex:
    
    #creating new vertex
    def __init__(self, x, y):
        #absolute position
        self.x = x
        self.y = y
        self.vel = 0


        #index used to identify the vertex in the graph
        self.index = 0

        self.grounded = False

        if self.y == 50:
            self.grounded = True


    #draws the vertex on the screen
    def draw_vertex(self, screen):
        
        pygame.draw.circle(screen, constants.vertex_color, (self.x, constants.SCREEN_HEIGHT - self.y), constants.vertex_radius)

    def write():
        print(constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH)
    