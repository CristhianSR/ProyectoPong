import tkinter as tk 

window =tk.Tk()

#Definición para que se pueda dar click en los botones
def on_button_click():
    print("Click en el boton")

#Características de la ventana
window.title("Atari Pong")
window.geometry("1420x720")
window.configure(background="#37525A")

#Ingreso de la imagen de menú
img=tk.PhotoImage(file="menu.png")
lbl_img= tk.Label(window, image=img)
lbl_img.pack()

#Creación de los botones
button1 = tk.Button (window, text="Iniciar Juego",bg="#EFF5D8", command=on_button_click)
button1.place(x=650, y=400, height=75, width=150)

button2 = tk.Button (window, text="Salir",bg="#EFF5D8", command=on_button_click)
button2.place(x=650, y=500, height=75, width=150)

window.mainloop()
