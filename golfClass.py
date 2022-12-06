import pygame

class Ball:
    '''class representing the golf ball'''
    def __init__(self, screen = None, coords = (250, 250), radius = 10, color = (255, 0, 0)):
        self.screen = screen
        self.coords = coords
        self.radius = radius
        self.color = color
        self.body = pygame.draw.circle(surface = screen, color = (255, 0 , 0), center = coords, radius = 50)
        self.velocity = (0, 0)
        self.active = False
        self.score = 0

    def setCoords(self, coords):
        self.coords = coords

    def draw(self):
        """draws balls"""
        pygame.draw.circle(surface = self.screen, color = self.color, center = self.coords, radius = self.radius)
        

    def update(self, velocity = (0,0)):
        if self.active:
            self.velocity = velocity
            self.score += sum([v**2 for v in velocity]) ** 0.5 #score will be the total distance traveled by the ball
            #self.velocity = (acc[0] + self.velocity[0], acc[1] + self.velocity[1])
            self.coords = (self.velocity[0] + self.coords[0], -self.velocity[1] + self.coords[1])
            self.draw()
        else:
            self.coords = pygame.mouse.get_pos()
            self.draw()


class Vfield():
    def __init__(self, image, f, xScale, yScale, xPix = 650, yPix = 650):
        """f takes two arguments and returns a tuple which represents the vector field"""
        self.f = f
        self.image = pygame.image.load(image)
        self.xPix = xPix
        self.yPix = yPix
        self.xScale = xScale
        self.yScale = yScale
        self.xwidth = self.xScale[1] - self.xScale[0]
        self.ywidth = self.yScale[1] - self.yScale[0]
        self.screen = pygame.display.set_mode((xPix, yPix))

    def updateScreen(self):
        self.screen.blit(self.image, (0,0))
    
    def transform(self, x, y):
        '''given coords x and y from screen coords returns coords (x, y) in function coords'''
        return (x*(self.xwidth/self.xPix) + self.xScale[0], -y*(self.ywidth/self.yPix) + self.yScale[1])
    
    def itransform(self,x,y):
        '''given coords x and y in function coords returns coods (x, y) in screen coords'''
        return ((x-self.xScale[0])*self.xPix/self.xwidth, (self.yScale[1] - y)*self.yPix/self.ywidth)
    
    def calc(self, coord):
        '''takes in screen coords. Returns the vector output by the vectorfield'''
        coord = self.transform(coord[0], coord[1])
        return self.f(coord[0],coord[1])

class Goal(Ball):

    def __init__(self, screen = None, coords = (250, 250), radius = 10, color = (0, 0, 0), isHit = False):
        super().__init__(screen, coords, radius, color = (0, 0, 0))
        self.isHit = isHit

    def madeGoal(self, ballCoords, radius):
        '''Checks if the ball and the goal are touching'''
        if ((self.coords[0]-ballCoords[0])**2 + (self.coords[1]-ballCoords[1])**2 <= (2*radius)**2):
            return True
            



#print('im still not stupid')



