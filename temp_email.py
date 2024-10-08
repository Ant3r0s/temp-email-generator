import requests
import json
import time

BASE_URL = "https://api.10minutemail.net"

def create_temp_email():
    response = requests.get(f"{BASE_URL}/api/create")
    if response.status_code == 200:
        email_data = response.json()
        return email_data
    else:
        print("Error creando el correo temporal.")
        return None

def get_inbox(email_id):
    time.sleep(10)  # Espera un momento para permitir que los correos lleguen
    response = requests.get(f"{BASE_URL}/api/mailbox?mailbox={email_id}")
    if response.status_code == 200:
        inbox_data = response.json()
        return inbox_data
    else:
        print("Error obteniendo el buzón de correo.")
        return None

def filter_and_display_emails(inbox, sender_filter=None, max_emails=None):
    if not inbox or 'messages' not in inbox:
        print("No se encontraron correos.")
        return

    print("Correos recibidos:")
    count = 0
    for message in inbox['messages']:
        if max_emails and count >= max_emails:
            break
        subject = message.get('subject', 'Sin asunto')
        sender = message.get('from', 'Desconocido')

        # Filtrar por remitente
        if sender_filter and sender_filter not in sender:
            continue

        print(f"De: {sender}, Asunto: {subject}")
        count += 1

if __name__ == "__main__":
    # Crear un correo temporal
    email_info = create_temp_email()
    if email_info:
        print("Correo temporal creado:")
        print(f"Email: {email_info['email']}")
        print(f"ID: {email_info['id']}")

        # Espera unos segundos y obtén el buzón de correo
        print("\nEsperando a que lleguen los correos...")
        inbox = get_inbox(email_info['id'])
        
        # Filtra y muestra los correos (ajusta el filtro y el límite según tus necesidades)
        filter_and_display_emails(inbox, sender_filter=None, max_emails=5)
