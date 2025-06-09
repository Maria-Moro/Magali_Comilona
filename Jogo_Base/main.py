import pygame
import random

# Inicialização do Pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROSA = (255, 100, 150)
PRETO = (0, 0, 0)

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Magali Comilona")

# Fonte
fonte = pygame.font.SysFont("Arial", 32)

# Magali (personagem)
magali_img = pygame.image.load("magali.png")  # Substitua por uma imagem pequena (ex: 64x64)
magali_img = pygame.transform.scale(magali_img, (64, 64))
magali_x = LARGURA // 2
magali_y = ALTURA // 2
velocidade = 5

# Fruta
fruta_raio = 20
fruta_x = random.randint(0, LARGURA - fruta_raio)
fruta_y = random.randint(0, ALTURA - fruta_raio)

# Pontuação
pontos = 0

# Relógio
relogio = pygame.time.Clock()

# Função para desenhar a fruta
def desenhar_fruta(x, y):
    pygame.draw.circle(tela, ROSA, (x, y), fruta_raio)

# Função para mostrar a pontuação
def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10, 10))

# Loop principal
jogando = True
while jogando:
    tela.fill(BRANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        magali_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        magali_x += velocidade
    if teclas[pygame.K_UP]:
        magali_y -= velocidade
    if teclas[pygame.K_DOWN]:
        magali_y += velocidade

    # Limites da tela
    magali_x = max(0, min(magali_x, LARGURA - 64))
    magali_y = max(0, min(magali_y, ALTURA - 64))

    # Desenhar Magali
    tela.blit(magali_img, (magali_x, magali_y))

    # Desenhar fruta
    desenhar_fruta(fruta_x, fruta_y)

    # Verificar colisão
    magali_centro_x = magali_x + 32
    magali_centro_y = magali_y + 32
    distancia = ((magali_centro_x - fruta_x) ** 2 + (magali_centro_y - fruta_y) ** 2) ** 0.5

    if distancia < fruta_raio + 32:
        pontos += 1
        fruta_x = random.randint(fruta_raio, LARGURA - fruta_raio)
        fruta_y = random.randint(fruta_raio, ALTURA - fruta_raio)

    # Moimport pygame
import random
import datetime
import speech_recognition as sr
import pyttsx3
from Recursos.funcoes import saudacao_jogador

# Inicializações
pygame.init()
engine = pyttsx3.init()

# Configuração da tela
LARGURA = 1000
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Magali Comilona")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROSA = (255, 100, 150)
AMARELO = (255, 255, 0)

# Recursos
fundo = pygame.image.load("Recursos/fundo.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
magali_img = pygame.image.load("Recursos/magali.png")
magali_img = pygame.transform.scale(magali_img, (64, 64))
fonte = pygame.font.SysFont("Arial", 32)

# Jogador
jogador = {"x": LARGURA//2, "y": ALTURA//2, "vel": 5, "pontos": 0}

# Fruta
fruta = {"raio": 20, "x": random.randint(50, 950), "y": random.randint(50, 650)}

# Sol pulsante
sol_raio = 40
raio_max = 60
raio_min = 30
pulsando = True

# Pausa
pausado = False

# Registro
def salvar_log(pontos):
    agora = datetime.datetime.now()
    with open("log.dat", "a") as f:
        f.write(f"{pontos} - {agora.strftime('%d/%m/%Y %H:%M:%S')}\n")

# Fala do jogo
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Reconhecimento de voz (simples)
def ouvir_nome():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga seu nome:")
        audio = recognizer.listen(source)
    try:
        nome = recognizer.recognize_google(audio, language="pt-BR")
        return nome
    except:
        return "Jogador"

# Boas-vindas
def tela_boas_vindas(nome):
    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))
        texto = fonte.render(f"Bem-vindo, {nome}!", True, PRETO)
        instrucoes = fonte.render("Use as setas para mover Magali. Coma as frutas!", True, PRETO)
        iniciar = fonte.render("Pressione ENTER para começar", True, PRETO)
        tela.blit(texto, (300, 200))
        tela.blit(instrucoes, (200, 300))
        tela.blit(iniciar, (250, 400))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    rodando = False

# Tela de fim de jogo
def tela_fim():
    tela.fill(BRANCO)
    texto = fonte.render("Fim de jogo! Últimos registros:", True, PRETO)
    tela.blit(texto, (300, 100))
    try:
        with open("log.dat", "r") as f:
            linhas = f.readlines()[-5:]
        for i, linha in enumerate(linhas):
            l = fonte.render(linha.strip(), True, PRETO)
            tela.blit(l, (300, 150 + i*40))
    except:
        tela.blit(fonte.render("Sem registros.", True, PRETO), (300, 150))
    pygame.display.update()
    pygame.time.wait(5000)

# Início
nome_jogador = ouvir_nome()
falar(f"Olá {nome_jogador}, prepare-se para comer muitas frutas!")
tela_boas_vindas(nome_jogador)

# Jogo principal
relogio = pygame.time.Clock()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            pausado = not pausado

    if not pausado:
        tela.blit(fundo, (0, 0))

        # Movimento
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador["x"] -= jogador["vel"]
        elif teclas[pygame.K_RIGHT]:
            jogador["x"] += jogador["vel"]
        elif teclas[pygame.K_UP]:
            jogador["y"] -= jogador["vel"]
        elif teclas[pygame.K_DOWN]:
            jogador["y"] += jogador["vel"]

        # Colisão
        dx = (jogador["x"] + 32) - fruta["x"]
        dy = (jogador["y"] + 32) - fruta["y"]
        if (dx**2 + dy**2)**0.5 < fruta["raio"] + 32:
            jogador["pontos"] += 1
            fruta["x"] = random.randint(50, 950)
            fruta["y"] = random.randint(50, 650)

        # Sol pulsante
        if pulsando:
            sol_raio += 0.5
            if sol_raio >= raio_max:
                pulsando = False
        else:
            sol_raio -= 0.5
            if sol_raio <= raio_min:
                pulsando = True

        pygame.draw.circle(tela, AMARELO, (80, 80), int(sol_raio))

        # Fruta e jogador
        pygame.draw.circle(tela, ROSA, (fruta["x"], fruta["y"]), fruta["raio"])
        tela.blit(magali_img, (jogador["x"], jogador["y"]))

        # Pontos
        pontos_txt = fonte.render(f"Pontos: {jogador['pontos']}", True, PRETO)
        pause_hint = fonte.render("Press Space to Pause Game", True, PRETO)
        tela.blit(pontos_txt, (10, 10))
        tela.blit(pause_hint, (750, 10))
    else:
        pausa_txt = fonte.render("PAUSE", True, PRETO)
        tela.blit(pausa_txt, (LARGURA//2 - 60, ALTURA//2 - 30))

    pygame.display.update()
    relogio.tick(60)

salvar_log(jogador["pontos"])
tela_fim()
pygame.quit()