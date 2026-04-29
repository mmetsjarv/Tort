import pygame
import math

pygame.init()

# Aken
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2 lisaülesanne - Metsjärv")

# Pildid

background = pygame.image.load("elutuba.png").convert_alpha()
background = pygame.transform.scale(background, (800, 600))

logo = pygame.image.load("VIKK logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (220, 40))

cake = pygame.image.load("cake.png").convert_alpha()
cake = pygame.transform.scale(cake, (150, 120))

sword = pygame.image.load("Mõõk.png").convert_alpha()
sword = pygame.transform.scale(sword, (100, 100))

# Font
font = pygame.font.SysFont("comicsansms", 30)

def draw_curved_text(surface, text, center, radius):
    for i, char in enumerate(text):
        angle = math.radians(270 + i * (180 / len(text)))
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)

        char_surf = font.render(char, True, (255, 255, 255))
        rect = char_surf.get_rect(center=(x, y))
        surface.blit(char_surf, rect)

running = True
while running:
    screen.fill((30, 30, 30))

    # background
    screen.blit(background, (0, 0))

    # Logo
    screen.blit(logo, (0, 0))

    # Kaarega tekst logo ümber
    draw_curved_text(screen, "TULEVIK 2050", (80, 80), 70)

    # Tort laual
    screen.blit(cake, (340, 310))

    # Mõõk seinal
    screen.blit(sword, (370, 75))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
