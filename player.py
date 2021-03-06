import sys

from tkinter import Tk, Button
from tkinter.font import Font
from copy import deepcopy

class Player:
  
  def __init__(self,other=None):
    self.player = 'O'
    self.ai = 'X'
    self.empty = ' '
    self.size = 3
    self.fields = {}
    self.score = 0
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty
    
    if other:
      self.__dict__ = deepcopy(other.__dict__)
      
  def tied(self):
    for (x,y) in self.fields:
      if self.fields[x,y]==self.empty:
        return False
    return True
  
  def won(self):
    # horizontal
    for y in range(self.size):
      winning = []
      for x in range(self.size):
        if self.fields[x,y] == self.ai:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    # vertical
    for x in range(self.size):
      winning = []
      for y in range(self.size):
        if self.fields[x,y] == self.ai:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    # diagonal
    winning = []
    for y in range(self.size):
      x = y
      if self.fields[x,y] == self.ai:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    # other diagonal
    winning = []
    for y in range(self.size):
      x = self.size-1-y
      if self.fields[x,y] == self.ai:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    # default
    return None 
  
  def move(self,x,y):
    board = Player(self)
    board.fields[x,y] = board.player
    (board.player,board.ai) = (board.ai,board.player)
    return board
  
  def __minimax(self, O):
    if self.won():
      if O:
        return (-5,None)
      else:
        return (+5,None)
    elif self.tied():
      return (0,None)
    elif O:
      best = (-10,None)
      for x,y in self.fields:
        if self.fields[x,y]==self.empty:
          value = self.move(x,y).__minimax(not O)[0]
          if value>best[0]:
            best = (value,(x,y))
      return best
    else:
      best = (+10,None)
      for x,y in self.fields:
        if self.fields[x,y]==self.empty:
          value = self.move(x,y).__minimax(not O)[0]
          if value<best[0]:
            best = (value,(x,y))
      return best
  
  def best(self):
    return self.__minimax(True)[0]
  
  def __str__(self):
    string = ''
    for y in range(self.size):
      for x in range(self.size):
        string+=self.fields[x,y]
      string+="\n"
    return string
        