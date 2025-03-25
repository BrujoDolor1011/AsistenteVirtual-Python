import os
import subprocess
import pyautogui
import time
import platform
import psutil
import webbrowser

def apagar_pc():
    os.system("shutdown /s /t 0")

def abrir_bloc_notas():
    subprocess.Popen(["notepad.exe"])

def capturar_pantalla(chat, root):
    root.iconify()  # Minimiza la ventana
    time.sleep(0.5)  # Espera un momento para que la minimización tenga efecto
    screenshot = pyautogui.screenshot()
    screenshot.save("captura.png")
    root.deiconify()  # Restaura la ventana
    chat.insert("end", "📸 Captura guardada como 'captura.png'\n", "info")

def info_sistema(chat):
    info = f"OS: {platform.system()} {platform.release()} | CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}%"
    chat.insert("end", f"💻 {info}\n", "info")

def abrir_web():
    webbrowser.open("https://www.google.com")
