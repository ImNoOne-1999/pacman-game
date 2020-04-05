import pygame
from settings import *
vec = pygame.math.Vector2

class Finder:
    def __init__(self,app,pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.personality = "catch"

    
    def update(self):
        self.pix_pos += self.direction
        if self.time_to_move():
            self.move()
            
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER +
                            self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER +
                            self.app.cell_height//2)//self.app.cell_height+1
        
        

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True
        return False

    def move(self):
        if self.personality == "catch":
            
            self.direction = self.get_path_direction()
            
                
        

    def draw(self):
        pygame.draw.circle(self.app.screen,(208,22,22),(int(self.pix_pos.x),int(self.pix_pos.y)),
        self.app.cell_width//2-2 )

        pygame.draw.rect(self.app.screen,RED,
        (self.grid_pos[0]*self.app.cell_width+TOP_BOTTOM_BUFFER//2,self.grid_pos[1]*self.app.cell_height+TOP_BOTTOM_BUFFER//2,self.app.cell_width,self.app.cell_height), 1)
        
        

    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,(self.grid_pos.y*self.app.cell_height)+TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)
    

    def get_path_direction(self):
        next_cell = self.find_next_cell_in_path()
        xdir = next_cell[0] - self.grid_pos[0]
        ydir = next_cell[1] - self.grid_pos[1]
        return vec(xdir,ydir)

    def find_next_cell_in_path(self):
        path = self.BFS([int(self.grid_pos.x),int(self.grid_pos.y)],[int(self.app.player.grid_pos.x),int(self.app.player.grid_pos.y)])
        pygame.draw.rect(self.app.background,(112,55,163),[int(self.grid_pos.x*self.app.cell_width),int(self.grid_pos.y*self.app.cell_height),self.app.cell_width,self.app.cell_height])
        return path[1]

    def BFS(self, start, target):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0, -1], [1, 0], [0, 1], [-1, 0]]
                for neighbour in neighbours:
                    if neighbour[0]+current[0] >= 0 and neighbour[0] + current[0] < len(grid[0]):
                        if neighbour[1]+current[1] >= 0 and neighbour[1] + current[1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    pygame.draw.rect(self.app.background,(12,55,13),[int(next_cell[0]*self.app.cell_width),int(next_cell[1]*self.app.cell_height),self.app.cell_width,self.app.cell_height])
                                    path.append({"Current": current, "Next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest