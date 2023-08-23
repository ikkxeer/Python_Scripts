# Aplicación Minotaurus v1.0

**Minotaurus** es una aplicación desarrollada con el framework Kivy en Python para enviar paquetes UDP a través de la red. Puedes utilizar esta aplicación para enviar paquetes a una dirección IP y un puerto especificados con diversas opciones de configuración.

## Requisitos

- Python
- Biblioteca Kivy (`pip install kivy`)

## Cómo Usar

1. Ejecuta la aplicación ejecutando el archivo `minotaurus.py`.
2. Aparecerá una interfaz gráfica con varios campos y botones.

   - **Dirección IP:** Ingresa la dirección IP de destino a la que deseas enviar los paquetes.
   - **Puerto:** Ingresa el puerto al que deseas enviar los paquetes. Valor predeterminado de 12345.
   - **Cantidad de Paquetes:** Ingresa la cantidad de paquetes que deseas enviar. Valor predeterminado de 100.
   - **Tamaño del Paquete:** Ingresa el tamaño del paquete en bytes. Valor predeterminado de 64.
   - **Tipo de Paquete:** Selecciona el tipo de paquete. (Solo se admite UDP en esta versión ya que estoy trabajando en agregar nuevos tipos distintos de paquetes)

3. Haz clic en el botón "ENVIAR" para enviar los paquetes según la configuración especificada. Minotaurus mostrará la cantidad de paquetes enviados y la cantidad de paquetes perdidos durante el transcurso de el enviamiento.

4. Opcionalmente, puedes utilizar el botón "Bucle Totalus" para enviar paquetes continuamente con un intervalo de 0.1 segundos

## Notas

- La aplicación utiliza sockets UDP para enviar los paquetes, estoy trabajando en implementar protocolos TCP y HTTP
- La aplicación se proporciona tal como está y no garantiza un rendimiento óptimo en todos los casos.
- Haré nuevas implementaciones en un futuro, tener en cuenta que estoy aun aprendiendo ^^

## Autor

Nombre: Ikkxeer
Contacto: samuiker2427@gmail.com
