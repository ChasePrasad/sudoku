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

    def draw(self):
        # finds the x, y, width, and height of each cell
        width = self.screen.get_width() // 9
        height = self.screen.get_height() // 9

        # finds the color when a cell is selected and draws the cell onto the screen
        color = None
        color = "red" if self.chosen else "black"
        pygame.draw.rect(self.screen, color, pygame.Rect(0, 0, 100, 100), 2)

        # displays a number when the cell has a value
        if self.value != 0:
            text = pygame.font.Font("font.ttf", 50).render(str(self.value), 1, "black")
            text_rect = text.get_rect(center=(width //2, height // 2))
            self.screen.blit(text, text_rect)

        # displays the sketched number for a cell
        elif self.sketched_value != 0:
            text = pygame.font.Font("font.ttf", 50).render(str(self.sketched_value), 1, (112, 98, 76))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            self.screen.blit(text, text_rect)



