import os

import pygame
import requests

map_file = "map.png"

z = 4
coords = [136.0, -28.0]
text = ''
screen = pygame.display.set_mode((600, 450))
server_address = 'https://static-maps.yandex.ru/v1?'
api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'


def object_search():
    global text, coords
    if k[pygame.K_BACKSPACE]:
        text = text[:-1]
        update(coords, z)
    if k[pygame.K_RETURN]:
        try:
            geocode = text
            geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=8013b162-6b42-4997-9691-77b7074026e0&geocode={geocode}&format=json'
            response = requests.get(geocoder_request)
            if response:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                toponym_coodrinates = toponym["Point"]["pos"]
                coords[0] = float(toponym_coodrinates.split()[0])
                coords[1] = float(toponym_coodrinates.split()[1])

                update(coords, z)
        except Exception:
            print(Exception)
    for event in pygame.event.get():
        if event.type == 771:
            text += event.text
            update(coords, z)

    pygame.font.init()
    font = pygame.font.Font(None, 36)
    text1 = font.render(text, True, (0, 0, 0))
    screen.blit(text1, (200, 0))
    pygame.display.update()


def update(coords, z):
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={str(coords[0])},{str(coords[1])}&z={z}'
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

    object_search()

pygame.quit()
os.remove(map_file)
