import os
import pygame
import requests

map_file = "map.png"


z = 4
coords = [136, -28]


def update(coords, z):
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={coords[0]},{coords[1]}&z={z}'
    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)
    with open(map_file, "wb") as file:
        file.write(response.content)

    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()


update(coords, z)


while pygame.event.wait().type != pygame.QUIT:
    k = pygame.key.get_pressed()
    if k[pygame.K_PAGEUP] == 1:
        z += 1
        update(coords, z)
    if k[pygame.K_PAGEDOWN] == 1:
        z -= 1
        update(coords, z)
    if k[pygame.K_UP] == 1:
        coords[1] += 1
        update(coords, z)
    if k[pygame.K_DOWN] == 1:
        coords[1] -= 1
        update(coords, z)
    if k[pygame.K_LEFT] == 1:
        coords[0] -= 1
        update(coords, z)
    if k[pygame.K_RIGHT] == 1:
        coords[0] += 1
        update(coords, z)


pygame.quit()
os.remove(map_file)