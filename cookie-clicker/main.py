import tkinter as tk    # importar tkinter
from funcions import *  # importar fitxer de funcions
from PIL import Image, ImageTk  # per carregar la imatge de la cookie

finestra = tk.Tk()  # crear la finestra principal del joc
finestra.title("Cookie Clicker")    # titol de la finestra
finestra.configure(bg="#2F6D94")    # color background

# estadístiques
etiqueta_cookies = tk.Label(finestra, text="Cookies: 0", font=("Arial", 16))    # mostra el numero de cookies
etiqueta_cookies.grid(row=0, column=0, sticky="w", padx=10, pady=5) # posició a la finestra
etiqueta_cps = tk.Label(finestra, text="Cookies/s: 0")  # mostra les cookies per segon (cps)
etiqueta_cps.grid(row=1, column=0, sticky="w", padx=10, pady=5)

# canvas per la cookie
canvas_cookie = tk.Canvas(
    finestra,
    width=250,
    height=250,
    bg="#2F6D94",
    highlightthickness=0
)
canvas_cookie.grid(row=2, column=0, padx=10, pady=20)   # posicio i espais

# carregar imatge de la cookie
img_normal_pil = Image.open("cookie_espectral.png").convert("RGBA").resize((250, 250))  # obrir la imatge, convertir-la en RGBA i ajustar tamany
img_cookie = ImageTk.PhotoImage(img_normal_pil) # format a tkinter
image_id = canvas_cookie.create_image(0, 0, anchor="nw", image=img_cookie)  # dibuixar la cookie
canvas_cookie.image = img_cookie    # guardar referencia
canvas_cookie.image_id = image_id   # guardar id per després poder canviar la imatge
canvas_cookie.tag_bind(image_id, "<Button-1>", lambda e: clicar())  # assignar cick a la cookie

# imatge de la cookie radioactiva
img_radio_pil = Image.open("cookie_radioactiva.png").convert("RGBA").resize((250, 250)) # les mateixes característiques que la cookie normal però aquesta és radioactiva
img_radio = ImageTk.PhotoImage(img_radio_pil)

# frames per botons de compres i powerups
f_botons = tk.Frame(finestra)   # botons
f_botons.grid(row=2, column=1, padx=10, pady=10)

f_compres = tk.Frame(f_botons)  # compres
f_compres.grid(row=0, column=0, padx=5)

f_powerups = tk.Frame(f_botons) # powerups
f_powerups.grid(row=0, column=1, padx=5)

# botons de compres
botons = {}
max_filas = 5   # maxim botons
for i, nom in enumerate(compres):   # sobre cada eina de compra
    fila = i % max_filas    # fila dins la columna
    columna = i // max_filas    # columna segons index
    boto = tk.Button(
        f_compres,
        width=20,
        command=lambda n=nom: comprar(n)    # enllaça el click amb la funció comprar
    )
    boto.grid(row=fila, column=columna, padx=5, pady=5)
    botons[nom] = boto  # guardar per actualitzar després

boto_powerup_click = tk.Button( # powerup de clics 
    f_powerups,
    text="Powerup Click x2 (Preu 100)",
    bg="#f0e581",
    width=22,
    command=lambda: millorar("click")
)
boto_powerup_click.pack(pady=5) # pack perquè es posi un a baix de l'altre

boto_powerup_avies = tk.Button( # powerup de avies
    f_powerups,
    text="Powerup Àvies x2 (Preu 500)",
    bg="#f0e581",
    width=22,
    command=lambda: millorar("avies")
)
boto_powerup_avies.pack(pady=5)

boto_powerup_granja = tk.Button(    # powerup de granges
    f_powerups,
    text="Powerup Granja x2 (Preu 1000)",
    bg="#f0e581",
    width=22,
    command=lambda: millorar("granja")
)
boto_powerup_granja.pack(pady=5)

iniciar(    # iniciar el joc
    finestra,
    etiqueta_cookies,
    etiqueta_cps,
    botons,
    boto_powerup_click,
    boto_powerup_avies,
    boto_powerup_granja,
    canvas_cookie,
    img_cookie,
    img_radio
)
finestra.mainloop() # iniciaar loop de la finestra