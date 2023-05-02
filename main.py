import pygame
from vertex import *
from edge import *
import constants
import presets.graph
import random
import buttons

#global variables
graph_configured = False
vertices = []
edges = []
nbors = []

mouse_is_pressed = False
whats_going_on = 'main_menu'

#colors
color1 = 'red'
color2 = 'blue'

turn = 1

def update_graph():

    for v in vertices:
        if v.y == 50:
            v.grounded = True
        else:
            v.grounded = False

    visited = {x : False for x in vertices}
    q = []
    
    for v in vertices:
        if v.grounded:
            q.append(v)
            visited[v] = True

    while(len(q) != 0):
        cur = q[0]

        for nbor in nbors[cur.index]:
            if not visited[nbor]:
                q.append(nbor)
                visited[nbor] = True
        q.pop(0)

    for v in vertices:
        if visited[v]:
            v.grounded = True


    for e in edges:
        e.grounded = False
    for v in vertices:
        if v.grounded:
            for e in edges:
                if e.base == v or e.tip == v:
                    e.grounded = True

    for v in vertices:
        if not v.grounded:
            v.vel += constants.accel
            v.y += v.vel


def configure_graph():
    global vertices
    global edges
    global nbors

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

        if e[2] == 1:
            edges.append(Edge(v1, v2, constants.colors[color1]))
        if e[2] == 2:
            edges.append(Edge(v1, v2, constants.colors[color2]))


        #edges.append(Edge(v1, v2, e[2]))

        nbors[v1.index].append(v2)
        nbors[v2.index].append(v1)

    for i in vertices:
        print(i.index, nbors[i.index])

def options(screen):
    global whats_going_on
    global mouse_is_pressed
    global color1
    global color2

    screen.fill('#2e6585')

    mouse_pos = pygame.mouse.get_pos()

    color1_img = pygame.image.load("Buttons/color1.png").convert_alpha()
    color2_img = pygame.image.load("Buttons/color2.png").convert_alpha()
    back_img = pygame.image.load("Buttons/back.png").convert_alpha()

    color1_button = buttons.Button(200, 325, color1_img, 5)
    color2_button = buttons.Button(570, 325, color2_img, 5)
    back_button = buttons.Button(1000,750, back_img, 3)

    color1_button.draw(screen)
    color2_button.draw(screen)
    back_button.draw(screen)


    #if color1_button.checkForInput(mouse_pos) == True:
    blue_color1_img = pygame.image.load("Color_Options/blue_color.png").convert_alpha()
    brown_color1_img = pygame.image.load("Color_Options/brown_color.png").convert_alpha()
    green_color1_img = pygame.image.load("Color_Options/green_color.png").convert_alpha()
    pink_color1_img = pygame.image.load("Color_Options/pink_color.png").convert_alpha()
    purple_color1_img = pygame.image.load("Color_Options/purple_color.png").convert_alpha()
    red_color1_img = pygame.image.load("Color_Options/red_color.png").convert_alpha()
    yellow_color1_img = pygame.image.load("Color_Options/yellow_color.png").convert_alpha()
    orange_color1_img = pygame.image.load("Color_Options/orange_color.png").convert_alpha()
    
    
    blue_color2_img = pygame.image.load("Color_Options/blue_color.png").convert_alpha()
    brown_color2_img = pygame.image.load("Color_Options/brown_color.png").convert_alpha()
    green_color2_img = pygame.image.load("Color_Options/green_color.png").convert_alpha()
    pink_color2_img = pygame.image.load("Color_Options/pink_color.png").convert_alpha()
    purple_color2_img = pygame.image.load("Color_Options/purple_color.png").convert_alpha()
    red_color2_img = pygame.image.load("Color_Options/red_color.png").convert_alpha()
    yellow_color2_img = pygame.image.load("Color_Options/yellow_color.png").convert_alpha()
    orange_color2_img = pygame.image.load("Color_Options/orange_color.png").convert_alpha()
    
    list_of_colors = ['blue', 'brown', 'green', 'pink', 'purple', 'red', 'yellow', 'orange']
    color1_button = {x:0 for x in list_of_colors}
    color2_button = {x:0 for x in list_of_colors}

    color1_button['blue'] = buttons.Button(300, 425, blue_color1_img, 5)
    color1_button['brown'] = buttons.Button(350, 425, brown_color1_img, 5)
    color1_button['green'] = buttons.Button(400, 425, green_color1_img, 5)
    color1_button['pink'] = buttons.Button(450, 425, pink_color1_img, 5)
    color1_button['purple'] = buttons.Button(300, 475, purple_color1_img, 5)
    color1_button['red'] = buttons.Button(350, 475, red_color1_img, 5)
    color1_button['yellow'] = buttons.Button(400, 475, yellow_color1_img, 5)
    color1_button['orange'] = buttons.Button(450, 475, orange_color1_img, 5)
    
    color2_button['blue'] = buttons.Button(670, 425, blue_color2_img, 5)
    color2_button['brown'] = buttons.Button(720, 425, brown_color2_img, 5)
    color2_button['green'] = buttons.Button(770, 425, green_color2_img, 5)
    color2_button['pink'] = buttons.Button(820, 425, pink_color2_img, 5)
    color2_button['purple'] = buttons.Button(670, 475, purple_color2_img, 5)
    color2_button['red'] = buttons.Button(720, 475, red_color2_img, 5)
    color2_button['yellow'] = buttons.Button(770, 475, yellow_color2_img, 5)
    color2_button['orange'] = buttons.Button(820, 475, orange_color2_img, 5)
    

    if mouse_is_pressed == True:
        if back_button.checkForInput(mouse_pos) == True:
            #main_menu(screen)
            whats_going_on = 'main_menu'

        for x in list_of_colors:
            if color1_button[x].checkForInput(mouse_pos):
                color2 = x
            if color2_button[x].checkForInput(mouse_pos):
                color1 = x

    for x in list_of_colors:
        if not x == color2:
            color2_button[x].draw(screen)

        if not x == color1:
            color1_button[x].draw(screen)


def play(screen):
    global whats_going_on
    global mouse_is_pressed

    screen.fill('#2e6585')

    mouse_pos = pygame.mouse.get_pos()

    levels_img = pygame.image.load("Buttons/levels.png").convert_alpha()
    level1_img = pygame.image.load("Levels/level1.png").convert_alpha()
    level2_img = pygame.image.load("Levels/level2.png").convert_alpha()
    level3_img = pygame.image.load("Levels/level3.png").convert_alpha()
    level4_img = pygame.image.load("Levels/level4.png").convert_alpha()
    level5_img = pygame.image.load("Levels/level5.png").convert_alpha()
    level6_img = pygame.image.load("Levels/level6.png").convert_alpha()
    level7_img = pygame.image.load("Levels/level7.png").convert_alpha()
    level8_img = pygame.image.load("Levels/level8.png").convert_alpha()
    level9_img = pygame.image.load("Levels/level9.png").convert_alpha()
    level10_img = pygame.image.load("Levels/level10.png").convert_alpha()
    back_img = pygame.image.load("Buttons/back.png").convert_alpha()

    levels_button = buttons.Button(20, 90, levels_img, 5)
    level1_button = buttons.Button(120, 300, level1_img, 3)
    level2_button = buttons.Button(320, 300, level2_img, 3)
    level3_button = buttons.Button(520, 300, level3_img, 3)
    level4_button = buttons.Button(720, 300, level4_img, 3)
    level5_button = buttons.Button(920, 300, level5_img, 3)
    level6_button = buttons.Button(120, 420, level6_img, 3)
    level7_button = buttons.Button(320, 420, level7_img, 3)
    level8_button = buttons.Button(520, 420, level8_img, 3)
    level9_button = buttons.Button(720, 420, level9_img, 3)
    level10_button = buttons.Button(920, 420, level10_img, 3)
    back_button = buttons.Button(1000,750, back_img, 3)

    levels_button.draw(screen)
    level1_button.draw(screen)
    level2_button.draw(screen)
    level3_button.draw(screen)
    level4_button.draw(screen)
    level5_button.draw(screen)
    level6_button.draw(screen)
    level7_button.draw(screen)
    level8_button.draw(screen)
    level9_button.draw(screen)
    level10_button.draw(screen)
    back_button.draw(screen)

    if mouse_is_pressed == True:
        if back_button.checkForInput(mouse_pos) == True:
            
            whats_going_on = 'main_menu'
        
        if level1_button.checkForInput(mouse_pos):
            whats_going_on = 'game'



def quit():
    pygame.quit()

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

    play_button.draw(screen)
    options_button.draw(screen)
    quit_button.draw(screen)

    if mouse_is_pressed == True:
        if play_button.checkForInput(mouse_pos) == True:
            whats_going_on = 'play'
        if options_button.checkForInput(mouse_pos) == True:
            whats_going_on = 'options'
        if quit_button.checkForInput(mouse) == True:
            whats_going_on = 'quit'


def game(screen):
    global turn
    global whats_going_on

    update_graph()

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
                    if (edge.color == constants.colors[color1] and turn == 1) or (edge.color == constants.colors[color2] and turn == 2):
                            
                        edges.remove(edge)
                        
                        nbors[edge.tip.index].remove(edge.base)
                        nbors[edge.base.index].remove(edge.tip)
                        
                        turn = 3 - turn

            edge_hovered = True

    #change mouse back to arrow
    if not edge_hovered:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    #draw vertices
    for v in vertices:
        v.draw_vertex(screen)

    w = check_win()
    if w == 1:
        print("Player 1 wins!")
    if w == 2:
        print("Player 2 wins!")


def check_win():
    global vertices
    global edges

    exists_col_1 = False
    exists_col_2 = False

    for edge in edges:
        if edge.grounded:
            if edge.color == constants.colors[color1]:
                exists_col_1 = True
            if edge.color == constants.colors[color2]:
                exists_col_2 = True

    if exists_col_1 and (not exists_col_2):
        return 1
    if exists_col_2 and (not exists_col_1):
        return 2
    return 0


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

        pygame.display.set_caption("Hackenbush")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_is_pressed = True
                
                


        #clear screen
        screen.fill('#000000')

        #game runs

        if whats_going_on == 'main_menu':
            main_menu(screen)

        if whats_going_on == 'play':
            play(screen)

        if whats_going_on == 'options':
            options(screen)

        if whats_going_on == 'quit':
            quit()

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
