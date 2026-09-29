import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com/api/webhooks/1554622141557768342/BjWA3aE5_jJSBly8TngEoYpY0s3P7v437kUpEkciE2L6fJgM_me_5HYCi1Q9rRLyZxK6")

data = {
    "content": (
        "¡Hola a todos! **¡Es hora de prepararse para la raid de este domingo!**\n\n"
        "Asegúrense de revisar su rotación y estar listos con tiempo.\n\n"
        "⏰ **Horarios de convocatoria:**\n"
        "🇨🇱 **Chile:** 21:00 hrs\n"
        "🇻🇪 **Venezuela:** 20:00 hrs\n"
        "🇨🇴 **Colombia:** 19:00 hrs\n"
        "🇲🇽 **México:** 18:00 hrs\n\n"
        "¡Nos vemos en el campo de batalla! 🔥"
    ),
    "embeds": [
        {
            "image": {
                "url": "https://i.imgur.com/SdU1QhA.png"
            }
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("¡Mensaje enviado con éxito!")
else:
    print(f"Error al enviar: {response.status_code}, {response.text}")
