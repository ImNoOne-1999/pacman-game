import pygame, sys
from settings import *
from player_class import *
from finder_class import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.playerFinder = []
        self.f_pos = []
        self.cell_width = MAZE_WIDTH//28
        self.cell_height = MAZE_HEIGHT//30
        self.player = Player(self,vec(1,1))
        self.walls = []
        self.load()
        self.find_player()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
   
    def draw_text(self,words,screen,pos,size,color,font_name,centered=False):
        font = pygame.font.SysFont(font_name,size)
        text = font.render(words,False,color)
        text_size = text.get_size()
        if centered:
            pos[0] -= text_size[0]//2
            pos[1] -= text_size[1]//2
        screen.blit(text,pos)

    def load(self):
        self.background = pygame.image.load('pacmanbg.png')
        self.background = pygame.transform.scale(self.background,(MAZE_WIDTH,MAZE_HEIGHT))
        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx) )
                    elif char == "F":
                        self.f_pos.append([xidx, yidx])


    def find_player(self):
        for pos in self.f_pos:
            self.playerFinder.append(Finder(self, vec(pos)))

    def draw_grid(self):
        #for x in range(WIDTH//self.cell_width):
        #    pygame.draw.line(self.background,GREY,(x*self.cell_width,0),(x*self.cell_width,HEIGHT))
        #for x in range(HEIGHT//self.cell_height):
        #    pygame.draw.line(self.background,GREY,(0,x*self.cell_height),(WIDTH,x*self.cell_height))
        #for wall in self.walls:
        #    pygame.draw.rect(self.background,(112,55,163),(wall.x*self.cell_width,wall.y*self.cell_height,self.cell_width,self.cell_height))
        pass

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
    
    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('PUSH SPACE BAR',self.screen,[WIDTH//2,HEIGHT//2-50],START_TEXT_SIZE,(170,132,58),START_FONT,centered=True)
        self.draw_text('PACMAN USING BFS',self.screen,[WIDTH//2,HEIGHT//2+50],START_TEXT_SIZE,(44,167,198),START_FONT,centered=True)
        self.draw_text('BFS PATH',self.screen,[4,0],START_TEXT_SIZE,(255,255,255),START_FONT)
        pygame.display.update()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))
    
    def playing_update(self):
        self.player.update()
        for finder in self.playerFinder:
            finder.update()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background,(TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        self.draw_grid()
        self.draw_text('Dynamic BFS',self.screen,[60,0],18,WHITE,START_FONT)
        self.player.draw()
        for finder in self.playerFinder:
            finder.draw()
        pygame.display.update()