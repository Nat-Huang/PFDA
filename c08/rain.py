import pygame

class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = 'Green'

def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    particle = Particle()
    particle2 = Particle(pos=(2, 2))
    print(particle.pos)
    print(particle2.pos)
    particle.pos = (3, 4)
    print(particle.pos)
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: some game logic
        # Render & Display 
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        surf = pygame.Surface((30, 30))
        green = pygame.Color(0, 255, 0)
        surf.fill(green)
        screen.blit(surf, (resolution[0]//2, resolution[1]//2))
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()