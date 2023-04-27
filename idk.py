import pygame, sys, random, time


class color():
    cPath = []
    path = []
    lastMove = "" #Defines the last move taken by the color: helps with findPathsReturn()
    uniquePath = []
    finalPath = []

    def __init__(self, x1, y1, x2, y2, board, color):
        self.startX = x1
        self.startY = y1
        self.endX = x2
        self.endY = y2
        self.board = board
        self.color = color
    
    #def addPath(self):
    #    self.cPath = findPathsReturn(self.board, self.path, self.startX, self.startY, self.endX, self.endY, "").copy()

    def addUniquePath(self, newPath):
        self.cPath = newPath.copy()
    
    def addFinalPath(self, newPath):
        self.finalPath = newPath.copy()