import subprocess
import tkinter as tk 

window =tk.Tk()

#Definición para que se pueda dar click en los botones
def open_pong():
 subprocess.run(["python", "pong.py"]) 

#Función para que las intrucciones nos salgan en otra pantalla
def game_instructions():
 instructions = tk.Toplevel(window)
 instructions.title("Instrucciones")
 instructions.geometry("1420x720")
 instructions.configure(background="#008080")

 text_instruc = """
    Bienvenido a Atari Pong.

    Instrucciones:
    1. Usa las teclas 'W' y 'S' para manejar la paleta del jugador 1.
    2. Usa las teclas '↑' y '↓' para manejar la paleta del jugador 2.
    3. Puedes pausar el juego con la tecla espaciadora
    3. Gana puntos cada vez que la pelota pasa a tu oponente.
    5. !El primero jugador que llegue a 5 puntos es el ganador!
    6. ¡Diviértete jugando!

    """
 #Label para ubicar el texto dentro de la pantalla de las instrucciones
 label_instruc= tk.Label(instructions,text=text_instruc, font=("San Francisco", 30), bg="#008080", fg="#E0FFFF")
 label_instruc.pack(pady=20)

 #Creación del botón para cerrar, en la pantalla de instruccionesa
 close_buttonn=tk.Button(instructions, text="Cerrar", command= instructions.destroy, bg="#EFF5D8")
 close_buttonn.place(x=650, y=600, height=75, width=150)

#Función para el tercer boton "Salir"
def close_window():
    window.destroy()

#Características de la ventana
window.title("Atari Pong")
window.geometry("1420x720")
window.configure(background="#008080")

#Ingreso de la imagen de menú
img=tk.PhotoImage(file="menu pong.png")
lbl_img= tk.Label(window, image=img)
lbl_img.pack()

#Creación de los botones del menú principal
button1 = tk.Button (window, text="Iniciar Juego",bg="#EFF5D8", command=open_pong)
button1.place(x=650, y=400, height=75, width=150)

button2 = tk.Button (window, text=" Instrucciones",bg="#EFF5D8", command=game_instructions)
button2.place(x=650, y=500, height=75, width=150)

button3 = tk.Button (window, text="Salir",bg="#EFF5D8", command=close_window)
button3.place(x=650, y=600, height=75, width=150)

window.mainloop()