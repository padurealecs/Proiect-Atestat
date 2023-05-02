import pygame
import constants

class Edge:
    
    def __init__(self, parent, child, color):
        
        self.base = parent
        self.tip = child

        self.color = color

        self.grounded = False

    def draw_edge(self, screen):
        pygame.draw.line(screen, self.color, (self.base.x, constants.SCREEN_HEIGHT - self.base.y), (self.tip.x, constants.SCREEN_HEIGHT - self.tip.y), constants.edge_width)

    def is_hovered(self):
        x, y = pygame.mouse.get_pos()
        x1 = self.base.x
        y1 = constants.SCREEN_HEIGHT - self.base.y
        x2 = self.tip.x
        y2 = constants.SCREEN_HEIGHT - self.tip.y

        #formula for distance from point to line given coords
        dist = ((x2 - x1) * (y1 - y) - (x1 - x) * (y2 - y1)) * ((x2 - x1) * (y1 - y) - (x1 - x) * (y2 - y1)) / ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
        if dist < 40 and x >= min(x1, x2) - 5 and x <= max(x1, x2) + 5 and y >= min(y1, y2) - 5 and y <= max(y1, y2) + 5:
            return 1
        return 0

    def draw_highlight(self, screen):

        #convert color from hex to rgb
        rgb = []
        for i in [1, 3, 5]:
            decimal = int(self.color[i : i + 2], 16)
            rgb.append(decimal)

        #tint the color    
        new_rgb = [x + int((255 - x) * constants.tint_percentage) for x in rgb]
        
        #change back to hex code
        new_rgb = '#{:02x}{:02x}{:02x}'.format(new_rgb[0], new_rgb[1], new_rgb[2])

        pygame.draw.line(screen, new_rgb, (self.base.x, constants.SCREEN_HEIGHT - self.base.y), (self.tip.x, constants.SCREEN_HEIGHT - self.tip.y), constants.highlight_width)