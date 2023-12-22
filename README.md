# ProyectoPong
Proyecto de lógica de programación

Fecha: 22/12/2023

Objetivo: Realizar el juego de Atari Pong mediante la implementación de los conocimientos obtenidos en clase, más las investigaciones necesarias para realizar el proyecto, el punto del juego es enfrentar dos jugadores y el que llegue al máximo de puntos sea el ganador.

El proyecto seleccionado por mi persona fue el juego de ATARI PONG, porque al ser un juego técnicamente básico a los tiempos actuales es muy reconocido a nivel mundial, creo que recrear este juego en Python no solo será un desafío emocionante, sino también una experiencia educativa y entretenida.

En archivo menu.py se encuentra el menú principal del juego, contamos con tres botones principales:
-Iniciar juego: Nos lleva a la ventana del archivo pong.py donde se encuentra el juego.
-Instrucciones: Este botón nos lleva a otra ventana con las instrucciones para los jugadores, esta ventana tiene un botón para cerrar la ventana
-Salir: Cierra la ventana del menú

Archivo pong.py
En este archivo encontramos todo lo relacionado al juego y sus mecánicas.
Partes a destacar:
-Tiene un puntaje máximo de 5 puntos
-Las paletas regresan a su posición original después de que se marque un punto de cada jugador
-Al final de la partida nos sale el jugador que ganó
-Tiene un botón de pausa (barra espaciadora) y esc para salir
-Las paletas fueron configuradas mediante un if para que no se salgan de la pantalla
-Tiene dos sonidos agregados, uno en pong. py para la colisión de las paletas y otro en menu.py de fondo, es del juego minecraft pero me gusta por eso lo puse.

