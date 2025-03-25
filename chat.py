from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def enviar_mensaje(chat, entrada):
    user_input = entrada.get()
    if user_input.strip():
        chat.insert("end", f"Tú: {user_input}\n", "user")
        entrada.delete(0, "end")

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "Eres un asistente útil."},
                          {"role": "user", "content": user_input}]
            )
            respuesta = response.choices[0].message.content
        except Exception as e:
            respuesta = f"⚠️ Error al conectar con OpenAI: {e}"

        chat.insert("end", f"Asistente: {respuesta}\n", "assistant")
