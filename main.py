import customtkinter as ctk
from chat import enviar_mensaje
from musica import reproducir_musica, pausar_reanudar, siguiente_cancion
from sistema import apagar_pc, abrir_bloc_notas, capturar_pantalla, info_sistema, abrir_web
from utilidades import obtener_ip, escuchar, hablar, fecha_hora, guardar_nota, leer_notas
from volumen import subir_volumen, bajar_volumen

# Configuración de la interfaz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Asistente Virtual")
root.geometry("600x600")

# Marco del chat
chat_frame = ctk.CTkFrame(root)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

chat = ctk.CTkTextbox(chat_frame, width=580, height=350, wrap="word")
chat.pack(pady=10, padx=10, fill="both", expand=True)

# Barra inferior
bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(fill="x", padx=10, pady=5)

entrada = ctk.CTkEntry(bottom_frame, width=400, placeholder_text="Escribe tu mensaje...")
entrada.pack(side="left", padx=5, pady=5, expand=True, fill="x")

btn_enviar = ctk.CTkButton(bottom_frame, text="Enviar", command=lambda: enviar_mensaje(chat, entrada))
btn_enviar.pack(side="right", padx=5, pady=5)

# Botones de funciones
btns = [
    ("⏻ Apagar", apagar_pc), ("📄 Bloc Notas", abrir_bloc_notas),
    ("🔊 Subir Vol.", subir_volumen), ("🔉 Bajar Vol.", bajar_volumen),
    ("📸 Captura", capturar_pantalla), ("💻 Info", info_sistema),
    ("🌐 Google", abrir_web), ("📡 IP", obtener_ip),
    ("🎙 Escuchar", escuchar), ("🗣 Hablar", hablar),
    ("📌 Guardar Nota", guardar_nota), ("📅 Fecha/Hora", fecha_hora),
    ("📖 Leer Notas", leer_notas), ("🎵 Reproducir", reproducir_musica),
    ("⏸ Pausar/Reanudar", pausar_reanudar), ("⏭ Siguiente", siguiente_cancion)
]

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(fill="x", padx=10, pady=5)

for i, (texto, comando) in enumerate(btns):
    if comando in [apagar_pc, abrir_bloc_notas, abrir_web]:
        btn = ctk.CTkButton(btn_frame, text=texto, command=comando)
    elif comando == guardar_nota or comando == hablar:
        btn = ctk.CTkButton(btn_frame, text=texto, command=lambda cmd=comando: cmd(chat, entrada))
    elif comando == capturar_pantalla:
        btn = ctk.CTkButton(btn_frame, text=texto, command=lambda cmd=comando: cmd(chat, root))
    else:
        btn = ctk.CTkButton(btn_frame, text=texto, command=lambda cmd=comando: cmd(chat))
    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="ew")

root.mainloop()
