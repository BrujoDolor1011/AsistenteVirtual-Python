import json
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

VOLUMEN_FILE = "volumen.json"

def obtener_control_volumen():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return interface.QueryInterface(IAudioEndpointVolume)

def cargar_volumen():
    try:
        with open(VOLUMEN_FILE, "r") as f:
            return json.load(f).get("volumen", 0.5)  # Volumen por defecto: 50%
    except FileNotFoundError:
        return 0.5

def guardar_volumen(valor):
    with open(VOLUMEN_FILE, "w") as f:
        json.dump({"volumen": valor}, f)

def cambiar_volumen(chat, incremento):
    volumen_control = obtener_control_volumen()
    volumen_actual = volumen_control.GetMasterVolumeLevelScalar()
    nuevo_volumen = max(0.0, min(1.0, volumen_actual + incremento))

    volumen_control.SetMasterVolumeLevelScalar(nuevo_volumen, None)
    guardar_volumen(nuevo_volumen)

    porcentaje = int(nuevo_volumen * 100)
    chat.insert("end", f"🔊 Volumen: {porcentaje}%\n", "info")

def subir_volumen(chat):
    cambiar_volumen(chat, 0.1)

def bajar_volumen(chat):
    cambiar_volumen(chat, -0.1)

# Cargar el volumen guardado al iniciar
volumen_inicial = cargar_volumen()
obtener_control_volumen().SetMasterVolumeLevelScalar(volumen_inicial, None)
