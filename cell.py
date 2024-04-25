
import pygame

# represents a single cell in the Sudoku board
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.column = col
        self.screen = screen
        self.sketched_value = 0
        self.chosen = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def get_sketched_value(self):
        return self.sketched_value

    # made by Murali Krishna Lingamsetty
    def get_value(self):
        return self.value

    def set_chosen(self, chosen):
        self.chosen = chosen

    def colored_cell(self, row, col):
        pygame.draw.rect(self.screen, (205, 173, 135), pygame.Rect(row * 60, col * 60, 60, 60), 3)
        pygame.draw.rect(self.screen, "black", pygame.Rect(row * 60, col * 60, 60, 60), 1)

    def draw(self):
        # finds the color when a cell is selected and draws the cell onto the screen
        color = "red" if self.chosen else "black"
        width = 3 if self.chosen else 1
        pygame.draw.rect(self.screen, color, pygame.Rect(self.row * 60, self.column * 60, 60, 60), width)

        # displays a number when the cell has a value
        if self.value != 0:
            text = pygame.font.Font("font.ttf", 25).render(str(self.value), 1, "black")
            text_rect = text.get_rect(center=(self.row * 60 + 30, self.column * 60 + 30))
            self.screen.blit(text, text_rect)

        # displays the sketched number for a cell
        elif self.sketched_value != 0:
            text = pygame.font.Font("font.ttf", 25).render(str(self.sketched_value), 1, (112, 98, 76))
            text_rect = text.get_rect(center=(self.row * 60 + 30, self.column * 60 + 30))
            pygame.draw.rect(self.screen, (205, 173, 135), pygame.Rect((self.row * 60 + 30) - 30 / 2, (self.column * 60 + 30) - 30 / 2, 35, 35))
            self.screen.blit(text, text_rect)

        # displays the sketched number for a cell
        elif self.sketched_value == 0:
            pygame.draw.rect(self.screen, (205, 173, 135), pygame.Rect((self.row * 60 + 30) - 30 / 2, (self.column * 60 + 30) - 30 / 2, 35, 35))

