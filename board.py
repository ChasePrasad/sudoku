import pygame
import math

from sudoku_generator import SudokuGenerator
from cell import Cell

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        #if self.difficulty == 1:
            #generator = SudokuGenerator(9, 30)
        #elif self.difficulty == 2:
            #generator = SudokuGenerator(9, 40)
        #else:
            #generator = SudokuGenerator(9, 50)

        generator = SudokuGenerator(9, 30)
        generator.fill_values()
        self.answerBoard = generator.get_board()
        generator.remove_cells()
        self.playerBoard = generator.get_board()

        self.boardList = [[0] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                self.boardList[i][j] = Cell(self.playerBoard[i][j], i, j, self.screen)

    def draw(self):
         for row in range(9):
            for col in range(9):
                self.boardList[row][col].draw()
                if (row != 0 and col != 0 and col % 3 == 0 and row % 3 == 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 60, 0), (col * 60, self.height - 60), 6)
                    pygame.draw.line(self.screen, (0, 0, 0), (0, row * 60), (self.width, row * 60), 6)

    def click(self):
        # determines whether player clicks inside game board.
        # Big if true: return True, x coordinate of click, y coordinate of click
        # Garbaje if false, return None
        coordinates = pygame.mouse.get_pos()
        if ((0 < coordinates[0] and coordinates[0] < 540) and (0< coordinates[1] and coordinates[1] < 540)):
            return True, coordinates[0], coordinates[1]
        else:
            return None

    #finds which cell is selected, returns x and y coordinates
    def select(self):
        self.status, self.xcoordinate, self.ycoordinate = self.click()
        if(self.status):
            self.selectedColumn = math.floor(float(self.xcoordinate / 60))
            self.selectedRow = math.floor(float(self.ycoordinate / 60))

            if(self.boardList[self.selectedRow][self.selectedColumn].getValue() != 0):
                #return True if player can edit
                return True, self.selectedColumn, self.selectedRow
            else:
                #return False if player CANNOT edit
                return False, self.selectedColumn, self.selectedRow
        else:
            return None

    def clear(self, row, col):
        Cell(0, row, col, self.screen)

    def sketch(self, value):
        self.sketchValue = value
        Cell.set_sketched_value(self.sketchValue)
        Cell.draw()

    def place_number(self, value):
        self.userInputColumn, self.userInputRow = self.select()
        self.boardList[self.UserInputRow][self.userInputColumn] = Cell(value, self.UserInputRow, self.userInputColumn, self.screen)
        self.update_board(value, self.UserInputRow, self.userInputColumn)

    def reset_to_original(self):
        for i in range(9):
            for j in range(9):
                self.boardList[i][j] = [Cell(self.playerBoard[i][j], i, j, self.screen)]

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.boardList[i][j].getValue() == 0:
                    return False
        return True
    def update_board(self, value, row, col):
        self.playerBoard[row][col] = value

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if(Cell.get_value(self.boardList[i][j]) == 0):
                    #returns row, column
                    return i, j
        return None

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if(Cell.get_value(self.boardList[i][j]) != self.answerBoard[i][j]):
                    return False

        return True
