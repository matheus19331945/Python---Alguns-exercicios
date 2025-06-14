#Importando bibliotecas necessárias
import pygame
# teste comentario
# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

# Carrega o arquivo MP3 que você deseja reproduzir
pygame.mixer.music.load("C:/Users/mathe/Downloads/thinking-time-148496.mp3")

# Reproduz o áudio carregado
pygame.mixer.music.play()

# Mantém o programa em execução até que a música termine de tocar
while pygame.mixer.music.get_busy():
    continue