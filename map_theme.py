import os
import pygame
import requests

map_file = "map.png"

z = 4
coords = [136, -28]
dark_theme = False
button_rect = pygame.Rect(10, 10, 30, 30)

def update(coords, z, dark_theme):
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={coords[0]},{coords[1]}&z={z}'
    theme_param = '&theme=dark' if dark_theme else ''
    map_request = f"{server_address}{ll_spn}{theme_param}&apikey={api_key}"
    response = requests.get(map_request)
    with open(map_file, "wb") as file:
        file.write(response.content)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.draw.rect(screen, (200, 0, 0), button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render("T", True, (255, 255, 255))
    screen.blit(text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()


update(coords, z, dark_theme)

running = True
while pygame.event.wait().type != pygame.QUIT:
    k = pygame.key.get_pressed()
    if k[pygame.K_PAGEUP] == 1:
        z += 1
        update(coords, z, dark_theme)
    if k[pygame.K_PAGEDOWN] == 1:
        z -= 1
        update(coords, z, dark_theme)
    if k[pygame.K_UP] == 1:
        coords[1] += 1
        update(coords, z, dark_theme)
    if k[pygame.K_DOWN] == 1:
        coords[1] -= 1
        update(coords, z, dark_theme)
    if k[pygame.K_LEFT] == 1:
        coords[0] -= 1
        update(coords, z, dark_theme)
    if k[pygame.K_RIGHT] == 1:
        coords[0] += 1
        update(coords, z, dark_theme)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                dark_theme = not dark_theme
                update(coords, z, dark_theme)


pygame.quit()
os.remove(map_file)