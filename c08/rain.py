import random
import pygame
import math


class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.age = 0 # in milliseconds
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        self.alpha = 255 * (math.sin(math.radians(self.age*0.5)) + 1) / 2

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)


def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    particle = Particle()
    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: some game logic
        particle.update(dt)
        # Render & Display
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        particle.draw(screen)
        pygame.display.flip()
        print(particle.age)
        dt = clock.tick()
    pygame.quit()


if __name__ == "__main__":
    main()