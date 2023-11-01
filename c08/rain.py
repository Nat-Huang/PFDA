import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: some game logic
        # Render & Display 
        screen.fill('Green')
    pygame.quit()


if __name__ == "__main__":
    main()