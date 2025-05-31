import pygame

pygame.init()
WIDTH, HEIGHT = 640, 640
square_size = WIDTH // 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Chess")
clock = pygame.time.Clock()

def get_valid_moves(board, row, col):
    piece = board[row][col]
    moves = []

    if piece == "":
        return moves

    color = piece[0]
    kind = piece[1]
    direction = -1 if color =="W" else 1

    if kind == "P":
        if board[row + direction][col] == "":
            moves.append((row + direction, col))

            if(color == "W" and row == 6) or (color == "B" and row == 1):
                if board[row + 2 * direction][col] == "":
                    moves.append((row + 2 * direction, col))
        
        if col > 0 and board[row + direction][col - 1].startswith("W" if color == "B" else "B"):
            moves.append((row + direction, col-1))
        if col < 7 and board[row + direction][col + 1].startswith("W" if color == "B" else "B"):
            moves.append((row + direction, col + 1))
    
    elif kind == "N":
        knight_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row - 1, col + 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        for r, c in knight_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if target == "" or target[0] != color:
                    moves.append((r, c))

    return moves

def load_image(name):
    img = pygame.image.load(f"assets/{name}.png")
    return pygame.transform.scale(img, (square_size, square_size))

pieces = {
    "BR": load_image("BRook"),
    "BN": load_image("BKnight"),
    "BB": load_image("BBishop"),
    "BQ": load_image("BQueen"),
    "BK": load_image("BKing"),
    "BP": load_image("BPawn"),
    "WR": load_image("WRook"),
    "WN": load_image("WKnight"),
    "WB": load_image("WBishop"),
    "WQ": load_image("WQueen"),
    "WK": load_image("WKing"),
    "WP": load_image("WPawn"),
}

board = [
    ["BR","BN","BB","BQ","BK","BB","BN","BR"],
    ["BP","BP","BP","BP", "BP", "BP", "BP", "BP"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["WP","WP","WP","WP", "WP", "WP", "WP", "WP"],
    ["WR","WN","WB","WQ","WK","WB","WN","WR"],
]
#Running
running = True

selected_square = None

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // square_size
            row = mouse_y // square_size

            if selected_square:
                src_row, src_col = selected_square
                piece = board[src_row][src_col]
                valid_moves = get_valid_moves(board, src_row, src_col)

                if (row, col) in valid_moves:
                    board[row][col] = piece
                    board[src_row][src_col] = ""
                selected_square = None
            else:
                if board[row][col] != "":
                    selected_square = (row, col)
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

            if selected_square == (row, col):
                highlight = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
                highlight.fill((255, 255, 0, 100))  # Yellow with transparency
                screen.blit(highlight, (x, y))

            piece = board[row][col]
            if piece in pieces:
                screen.blit(pieces[piece], (x, y))

    pygame.display.flip()

pygame.quit()
