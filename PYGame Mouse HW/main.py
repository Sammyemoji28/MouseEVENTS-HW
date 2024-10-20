
import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill((182,245,238))
pygame.display.update()

class Rectangle:
    def __init__(self, color, w, l, pos):
        self.color = color
        self.width = w
        self.length = l
        self.position = pos
        self.thickness = 3
        self.surface = screen
    def drawR(self, w, l):
        self.r = pygame.draw.rect(self.surface, self.color, (self.position[0], self.position[1], l, w))
    def increaseR(self, l, w):
        self.width += w
        self.length += l
        self.r = pygame.draw.rect(self.surface, self.color, (self.position[0], self.position[1], self.length, self.width))

rectangle = Rectangle("white", 15, 10, (250,250))

while True:
    screen.fill((182,23,49))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((126,38,152))
            rectangle.drawR(5,5)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((152,38,126))
            rectangle.increaseR(5,5)
            pygame.display.update()