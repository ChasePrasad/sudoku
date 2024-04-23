import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sudoku")
screen.fill((205, 173, 135))

def main():
    draw_game_start()
    
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    exit()

                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_s:
                            draw_game_start()

                        case pygame.K_w:
                            draw_game_won()
                            
                        case pygame.K_o:
                            draw_game_over()

                        case pygame.K_r:
                            draw_game_run()

        pygame.display.update()

def draw_game_start():
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    welcome_surf = pygame.font.Font("font.ttf", 75).render("Welcome to Sudoku", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(400, 324))
    screen.blit(welcome_surf, welcome_rect)

    mode_surf = pygame.font.Font("font.ttf", 50).render("Select Game Mode:", 1, "black")
    mode_rect = mode_surf.get_rect(center=(400, 470))
    screen.blit(mode_surf, mode_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(200, 525, 100, 50))
    easy_surf = pygame.font.Font("font.ttf", 25).render("Easy", 1, "black")
    easy_rect = easy_surf.get_rect(center=(250, 550))
    screen.blit(easy_surf, easy_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(350, 525, 100, 50))
    medium_surf = pygame.font.Font("font.ttf", 25).render("Medium", 1, "black")
    medium_rect = medium_surf.get_rect(center=(400, 550))
    screen.blit(medium_surf, medium_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(500, 525, 100, 50))
    hard_surf = pygame.font.Font("font.ttf", 25).render("Hard", 1, "black")
    hard_rect = hard_surf.get_rect(center=(550, 550))
    screen.blit(hard_surf, hard_rect)

def draw_game_won():
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    won_surf = pygame.font.Font("font.ttf", 75).render("Game Won!", 1, "black")
    won_rect = won_surf.get_rect(center=(400, 324))
    screen.blit(won_surf, won_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(350, 400, 100, 50))
    exit_surf = pygame.font.Font("font.ttf", 25).render("Exit", 1, "black")
    exit_rect = exit_surf.get_rect(center=(400, 425))
    screen.blit(exit_surf, exit_rect)

def draw_game_over():
    screen.blit(pygame.image.load("bg.jpg"), (0, 0))

    welcome_surf = pygame.font.Font("font.ttf", 75).render("Game Over :(", 1, "black")
    welcome_rect = welcome_surf.get_rect(center=(400, 324))
    screen.blit(welcome_surf, welcome_rect)

    pygame.draw.rect(screen, "white", pygame.Rect(350, 400, 100, 50))
    restart_surf = pygame.font.Font("font.ttf", 25).render("Restart", 1, "black")
    restart_rect = restart_surf.get_rect(center=(400, 425))
    screen.blit(restart_surf, restart_rect)

def draw_game_run():
    screen.fill((205, 173, 135))


if __name__ == "__main__":
    main()
