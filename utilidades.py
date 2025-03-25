import requests
import speech_recognition as sr
import pyttsx3
from datetime import datetime

def obtener_ip(chat):
    try:
        ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
        chat.insert("end", f"📡 IP Pública: {ip}\n", "info")
    except:
        chat.insert("end", "⚠️ No se pudo obtener la IP.\n", "info")

def escuchar(chat):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        chat.insert("end", "🎙 Escuchando...\n", "info")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        chat.insert("end", f"Tú (voz): {texto}\n", "user")
    except:
        chat.insert("end", "⚠️ No se pudo reconocer la voz.\n", "info")

def hablar(chat, entrada):
    texto = entrada.get()
    if texto.strip():
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
        chat.insert("end", "🗣 Reproduciendo voz...\n", "info")

def fecha_hora(chat):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat.insert("end", f"📅 {ahora}\n", "info")

def guardar_nota(chat, entrada):
    texto = entrada.get()
    if texto.strip():
        with open("notas.txt", "a") as f:
            f.write(texto + "\n")
        chat.insert("end", "📌 Nota guardada.\n", "info")

def leer_notas(chat):
    try:
        with open("notas.txt", "r") as f:
            notas = f.read()
        chat.insert("end", f"📖 Notas guardadas:\n{notas}\n", "info")
    except FileNotFoundError:
        chat.insert("end", "⚠️ No hay notas guardadas.\n", "info")
