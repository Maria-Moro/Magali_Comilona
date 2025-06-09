import pygame

def pulsar_sol(screen, frame):
    amarelo = (255, 255, 0)
    tamanho = 30 + 5 * abs(pygame.math.sin(frame / 20))
    pygame.draw.circle(screen, amarelo, (80, 80), int(tamanho))