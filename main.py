import pygame

WIDTH, HEIGHT = 640, 640

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Chess")

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ChessBoard
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = (240, 217, 181)
            else:
                color = (181, 136, 99)
            
            square_size = WIDTH // 8
            x = col * square_size
            y = row * square_size
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

    pygame.display.flip()

pygame.quit()
