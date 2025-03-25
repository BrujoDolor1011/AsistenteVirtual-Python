import pygame
import os
import random

pygame.mixer.init()
canciones = []
pausado = False  # Variable global para rastrear el estado de pausa

def cargar_canciones():
    global canciones
    if os.path.exists("musica/"):
        canciones = [f for f in os.listdir("musica/") if f.endswith(".mp3")]
        random.shuffle(canciones)

def reproducir_musica(chat):
    global pausado
    if not canciones:
        chat.insert("end", "⚠️ No hay canciones disponibles.\n", "info")
        return
    pygame.mixer.music.load(os.path.join("musica/", canciones[0]))
    pygame.mixer.music.play()
    chat.insert("end", f"🎵 Reproduciendo: {canciones[0]}\n", "info")
    pausado = False  # Resetear la variable al iniciar una nueva canción

def siguiente_cancion(chat):
    global pausado
    if canciones:
        canciones.append(canciones.pop(0))
        pygame.mixer.music.load(os.path.join("musica/", canciones[0]))
        pygame.mixer.music.play()
        chat.insert("end", f"⏭ Siguiente: {canciones[0]}\n", "info")
        pausado = False  # Asegurar que no quede en estado pausado

def pausar_reanudar(chat):
    global pausado
    if pausado:
        pygame.mixer.music.unpause()
        chat.insert("end", "▶ Música reanudada.\n", "info")
    else:
        pygame.mixer.music.pause()
        chat.insert("end", "⏸ Música pausada.\n", "info")
    pausado = not pausado  # Alternar el estado

cargar_canciones()
