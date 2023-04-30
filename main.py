import pygame
from vertex import *
from edge import *
import constants
#import presets.graph
import random
import buttons

#global variables
graph_configured = False
vertices = []
edges = []
nbors = []

mouse_is_pressed = False
whats_going_on = 'main_menu'

def configure_random_graph():

    global vertices
    global edges

    vertices = []
    edges = []


    for i in range(10):
        vertices.append(Vertex(random.randint(20, 1200), random.randint(0, 900)))

    for i in range(20):
        
        r1 = random.randint(1, 9)
        r2 = random.randint(0, r1 - 1)
        rand_num = random.randint(1118481,16777215)
        rand_hex = '#' + str(hex(rand_num))[2:]
        edges.append(Edge(vertices[r1], vertices[r2], rand_hex))
        print(rand_hex)
    

def configure_graph():
    global vertices
    global edges

    vertices = []
    edges = []
    
    indexx = 0
    for v in presets.graph.graph_v:
        vertices.append(Vertex(v[0], v[1]))
        vertices[indexx].index = indexx
        indexx += 1

    nbors = [[] for v in vertices]

    for e in presets.graph.graph_e:
        v1 = vertices[e[0]]
        v2 = vertices[e[1]]

        edges.append(Edge(v1, v2, e[2]))
        
        nbors[v1.index].append(v2)
        nbors[v2.index].append(v1)

    for i in vertices:
        print(i.index, nbors[i.index])


def main_menu(screen):
    
    global whats_going_on
    global mouse_is_pressed
    
    mouse_pos = pygame.mouse.get_pos()

    screen.fill('#2e6585')
    
    play_img = pygame.image.load("Buttons/play_button.png").convert_alpha() 
    options_img = pygame.image.load("Buttons/options_button.png").convert_alpha()
    quit_img = pygame.image.load("Buttons/quit_button.png").convert_alpha()

    play_button = buttons.Button(470,180, play_img, 5)
    options_button = buttons.Button(470,360,options_img, 5)
    quit_button = buttons.Button(470,540,quit_img,5)

    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.checkForInput(mouse_pos) == True:
                    screen.fill('#2e6585')
                    play_button.draw(screen)
                    options_button.draw(screen)
                    quit_button.draw(screen)
        

def game(screen):

    #draw base line
    draw_base_line(screen)

    #draw edges (should happen before drawing vertices)
    for edge in edges:
        edge.draw_edge(screen)

    edge_hovered = False
    for edge in edges:
        
        #check if edges are covered (only hover one)
        if edge.is_hovered():

            #hover the first edge
            if not edge_hovered:

                #change cursor to hover mode
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

                #draw the highlight then redraw the edge
                edge.draw_highlight(screen)
                edge.draw_edge(screen)

                if mouse_is_pressed:
                    edges.remove(edge)
                    #!!REMOVE FROM ADJACENDY LIST

                #remove the edge (EXPERIMENTAL)
                #edges.remove(edge)

            edge_hovered = True
    
    #change mouse back to arrow
    if not edge_hovered:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    #draw vertices
    for v in vertices:
        v.draw_vertex(screen)

    


def main():

    global graph_configured
    global mouse_is_pressed
    global whats_going_on

    #make a screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    #make a clock for limited framerate
    clock = pygame.time.Clock()

    #make game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_pressed = True
                print("hatz")


        #clear screen
        screen.fill('#000000')

        #game runs

        if whats_going_on == 'main_menu':
            main_menu(screen)

        elif whats_going_on == 'game':

            #configure graph if necessary (when opening a new game)
            #print(graph_configured) !REMOVE THIS
            if not graph_configured:
                configure_graph()
                graph_configured = True

            game(screen)
        
        pygame.display.flip()

        #final resets
        mouse_is_pressed = False

        #clock ticks with framerate
        clock.tick(constants.FPS)



if __name__ == "__main__":
    main()