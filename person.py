from pygame import Rect as Rect
import pygame


class person(pygame.Rect):
    def __init__(self, X, Y, width, height, genotype, awareness, xdirection, ydirection, color, bred=False, kill=False, age=0, childcount=0):
        Rect.__init__(self, X, Y, width, height)
        self.geno = genotype
        self.aware = awareness
        self.xdir = xdirection
        self.ydir = ydirection
        self.col = color
        self.breed = bred
        self.k = kill
        self.age = age
        self.children = childcount