import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

def guardar_pelicula():
    titulo = entrada_titulo.get()
    sipnosis = cuadro_sipnosis.get("1.0", tk.END)
    anio = entrada_anio.get()
    genero = entrada_genero.get()
    director = entrada_director.get()
    donde_ver = entrada_donde_ver.get()

    conexion = sqlite3.connect("peliculas.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO peliculas (titulo, sipnosis, anio, genero, director, donde_ver) VALUES (?, ?, ?, ?, ?, ?)",
                   (titulo, sipnosis, anio, genero, director, donde_ver))
    conexion.commit()
    conexion.close()

    mensaje = f"Película añadida correctamente:\nTítulo: {titulo}\nSinopsis: {sipnosis}\nAño: {anio}\nGénero: {genero}\nDirector: {director}\nDonde ver: {donde_ver}"
    messagebox.showinfo("Éxito", mensaje)
    
def abrir_ventana_agregar_pelicula():
    global entrada_titulo, cuadro_sipnosis, entrada_anio, entrada_genero, entrada_director, entrada_donde_ver
    
    ventana_agregar_pelicula = tk.Toplevel(root)
    ventana_agregar_pelicula.title("Agregar Película")
    ventana_agregar_pelicula.geometry("1080x500")

    imagen_fondo = Image.open("fondo2.png")
    imagen_fondo = imagen_fondo.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    
    fondo_label = tk.Label(ventana_agregar_pelicula, image=imagen_fondo, bd=0)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    formulario_frame = tk.Frame(ventana_agregar_pelicula, bg="white", width=320, height=320)
    formulario_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    etiqueta_titulo = tk.Label(formulario_frame, text="Título:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_titulo.grid(row=0, column=0, padx=10, pady=5)
    entrada_titulo = tk.Entry(formulario_frame, font=("Arial", 14))
    entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

    etiqueta_sipnosis = tk.Label(formulario_frame, text="Sinopsis:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_sipnosis.grid(row=1, column=0, padx=10, pady=5)
    cuadro_sipnosis = tk.Text(formulario_frame, height=5, width=40, font=("Arial", 14))
    cuadro_sipnosis.grid(row=1, column=1, padx=10, pady=5)

    etiqueta_anio = tk.Label(formulario_frame, text="Año:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_anio.grid(row=2, column=0, padx=10, pady=5)
    entrada_anio = tk.Entry(formulario_frame, font=("Arial", 14))
    entrada_anio.grid(row=2, column=1, padx=10, pady=5)

    etiqueta_genero = tk.Label(formulario_frame, text="Género:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_genero.grid(row=3, column=0, padx=10, pady=5)
    entrada_genero = tk.Entry(formulario_frame, font=("Arial", 14))
    entrada_genero.grid(row=3, column=1, padx=10, pady=5)

    etiqueta_director = tk.Label(formulario_frame, text="Director:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_director.grid(row=4, column=0, padx=10, pady=5)
    entrada_director = tk.Entry(formulario_frame, font=("Arial", 14))
    entrada_director.grid(row=4, column=1, padx=10, pady=5)

    etiqueta_donde_ver = tk.Label(formulario_frame, text="Donde ver:", fg="black", bg="white", font=("Arial", 16))
    etiqueta_donde_ver.grid(row=5, column=0, padx=10, pady=5)
    entrada_donde_ver = tk.Entry(formulario_frame, font=("Arial", 14))
    entrada_donde_ver.grid(row=5, column=1, padx=10, pady=5)

    boton_guardar = tk.Button(formulario_frame, text="Guardar", command=guardar_pelicula, bg="green", fg="white", font=("Arial", 16))
    boton_guardar.grid(row=6, column=0, columnspan=2, padx=10, pady=20)
    
def abrir_ventana_ver_peliculas_agregadas():
    ventana_ver_peliculas = tk.Toplevel(root)
    ventana_ver_peliculas.title("Ver Películas Agregadas")
    ventana_ver_peliculas.geometry("1080x500")

    # Código para mostrar la información de las películas agregadas
    conexion = sqlite3.connect("peliculas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()
    conexion.close()

    imagen_fondo = Image.open("fondo1.png")
    imagen_fondo = imagen_fondo.resize((ventana_ver_peliculas.winfo_screenwidth(), ventana_ver_peliculas.winfo_screenheight()))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    
    fondo_label = tk.Label(ventana_ver_peliculas, image=imagen_fondo, bd=0)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    tabla_frame = tk.Frame(ventana_ver_peliculas, bg="black")
    tabla_frame.pack(fill=tk.BOTH, expand=True)

    encabezados = ["ID", "Título", "Año", "Género", "Director", "Donde Ver"]
    for col, encabezado in enumerate(encabezados):
        tk.Label(tabla_frame, text=encabezado, fg="white", bg="black", relief=tk.RIDGE, width=15).grid(row=0, column=col, sticky="nsew")

    conexion = sqlite3.connect("peliculas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()
    conexion.close()

    for fila, pelicula in enumerate(peliculas, start=1):
        for col, valor in enumerate(pelicula):
            tk.Label(tabla_frame, text=valor, fg="white", bg="black", relief=tk.RIDGE, width=15).grid(row=fila, column=col, sticky="nsew")

# Configuración de la ventana principal
root = tk.Tk()
root.title("FilmFinder")
root.geometry("1080x500")
root.configure(bg="black")

imagen_fondo = Image.open("fondo1.png")
imagen_fondo = imagen_fondo.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

fondo_label = tk.Label(root, image=imagen_fondo, bd=0)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

etiqueta_bienvenida = tk.Label(root, text="¡Bienvenido a FilmFinder!", font=("Arial", 18), fg="white", bg="navyblue")
etiqueta_bienvenida.pack(pady=50)

boton_agregar_pelicula = tk.Button(root, text="Agregar Películas", command=abrir_ventana_agregar_pelicula, bg="navyblue", fg="white", font=("Arial", 16))
boton_agregar_pelicula.pack(pady=20)

boton_ver_info = tk.Button(root, text="Ver Peliculas Agregadas", command=abrir_ventana_ver_peliculas_agregadas, bg="navyblue", fg="white", font=("Arial", 16))
boton_ver_info.pack(pady=20)

etiqueta_footer = tk.Label(root, text="Creado por el Grupo 4 - SIC2023", font=("Arial", 18), fg="white", bg="navyblue")
etiqueta_footer.pack(pady=50)

root.mainloop()