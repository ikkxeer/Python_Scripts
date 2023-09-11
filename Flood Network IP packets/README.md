# Flood IP TCP packets

## Descripción
Este script Python utiliza la biblioteca Scapy para enviar paquetes de red a una dirección IP y puerto de destino especificados. Los paquetes enviados se crean con un encabezado TCP y datos dentro del paquete. El propósito de este script es proporcionar una herramienta para generar tráfico de red simulado.

## Requisitos
- Python 3.x
- Biblioteca Scapy (asegúrese de que esté instalada)

## Uso
1. Asegúrese de que Python 3.x esté instalado en su sistema.

2. Instale la biblioteca Scapy si aún no está instalada. Puede hacerlo utilizando pip:

3. Edite el script y configure los siguientes parámetros según sus necesidades:

   - `ip_destino`: La dirección IP de destino a la que se enviarán los paquetes.
   - `puerto_destino`: El puerto de destino por el que entrarán los paquetes.
   - `datos`: Los datos que se incluirán en cada paquete. En el ejemplo, se están enviando 1024 bytes de datos representados por "X".

4. Ejecute el script:
python main.py

5. El script generará paquetes de red simulados y los enviará a la dirección IP y puerto de destino especificados. Los paquetes se imprimirán en la consola a medida que se envíen.

## Importante
Este script es solo para fines educativos o de prueba. El uso indebido de este script para enviar tráfico no deseado a redes o sistemas ajenos puede ser ilegal y está sujeto a sanciones legales.

## Créditos
Este script utiliza la biblioteca Scapy, que es una herramienta de manipulación de paquetes de red escrita en Python. Para obtener más información sobre Scapy, visite [https://scapy.net/](https://scapy.net/).

## Autor
Nombre: Ikkxeer
Contacto: samuiker2427@gmail.com


