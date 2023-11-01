import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Rain") # Give our window a title
    resolution = (800, 600) 
    screen = pygame.display.set_mode(resolution) # Set the resolution of our screen surface.

if __name__ == "__main__":
    main()