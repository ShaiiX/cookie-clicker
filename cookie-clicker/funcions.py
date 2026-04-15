import tkinter as tk

# variables globals
cookies = 0 # total de cookies
cookies_seg = 0 # cookies per segon
valor_clic = 1  # valor del click manual
valor_clic_original = 1 # guardar valor original per restaurar després del radioactiu

boto_radio = None   # botó de cookie radioactiva
cooldown_radio = 0  # cooldown per tornar a activar radioactiu
radio_actiu = 0    # durada activada del radioactiu
cookie_normal = None    # imatge normal de la cookie
cookie_radio = None # imatge de la radioactiva
canvas_cookie = None    # canvas per poder canviar les imatges

compres = { # eines i compres amb nom, preu, cps i quantitat
    "Cursor":{"preu": 10, "cps": 1, "quantitat": 0},
    "Àvies":{"preu": 50, "cps": 5, "quantitat": 0},
    "Granja": {"preu": 100, "cps": 10, "quantitat": 0},
    "Mina": {"preu": 500, "cps": 50, "quantitat": 0},
    "Fàbrica": {"preu": 1000, "cps": 100, "quantitat": 0},
    "Banc": {"preu": 5000, "cps": 500, "quantitat": 0},
    "Temple": {"preu": 10000, "cps": 1000, "quantitat": 0},
    "Torre Màgica": {"preu": 50000, "cps": 5000, "quantitat": 0},
    "Cohet": {"preu": 100000, "cps": 10000, "quantitat": 0},
    "MEGA PRO MAX": {"preu": 500000, "cps": 50000, "quantitat": 0}
}

colors_compres = {  # colors dels botons segons el tipus de compra
    "Cursor": "#AAF0D1",
    "Àvies": "#FFD1DC",
    "Granja": "#FFFACD",
    "Mina": "#FFDAB9",
    "Fàbrica": "#FFAAA5",
    "Banc": "#B0E0E6",
    "Temple": "#FFDD94",
    "Torre Màgica": "#DCD0FF",
    "Cohet": "#8BCEF7",
    "MEGA PRO MAX": "#FF00B3"
}

powerups = {    # powerups per millorar les cookies
    "click": {"preu": 100, "cooldown": 0, "target": "Cursor"},
    "avies": {"preu": 500, "cooldown": 0, "target": "Àvies"},
    "granja": {"preu": 1000, "cooldown": 0, "target": "Granja"}
}

def clicar():   # quan es clica la cookie
    global cookies
    cookies += valor_clic
    actualitzar_pantalla()  # actualitza

def auto_sum(): # suma automàticament les cookies segons els cps (clics per segon)
    global cookies
    cookies += cookies_seg
    actualitzar_pantalla()
    finestra.after(1000, auto_sum)  # repetir cada  segon

def comprar(nom):   # comprar eina
    global cookies, cookies_seg
    item = compres[nom]
    if cookies >= item["preu"]: # comprova si tens prous diners
        cookies -= item["preu"] # resta el preu
        cookies_seg += item["cps"]  # augmenta la producció
        item["quantitat"] += 1  # suma un edifici més
        item["preu"] = int(item["preu"] * 1.15) # el proper serà més car
    actualitzar_pantalla()

def format_num(num):    # format de números grans
    if num >= 1_000_000:
        return str(round(num / 1_000_000, 1)) + "M" # quan arriba al milió es posa una M darrere
    if num >= 1_000:
        return str(round(num / 1_000, 1)) + "K" # quan arriba a mil es posa la K
    return str(num)


def millorar(nom):
    global cookies, cookies_seg, valor_clic
    p = powerups[nom]
    if p["cooldown"] > 0 or cookies < p["preu"]:    # no es pot comprar si hi ha cooldown o no hi ha cookies
        return
    cookies -= p["preu"]
    if nom == "click":
        valor_clic *= 2 # duplica el valor del click
    target = p["target"]
    extra = compres[target]["cps"] * compres[target]["quantitat"]
    compres[target]["cps"] *= 2 # duplica la base de producció de l'edifici
    cookies_seg += extra    # afegeix un nou extra a la producció global
    p["preu"] = int(p["preu"] * 1.5)    # puja preu del powerup
    p["cooldown"] = 60  # bloqueja el botó durant 60 seg
    actualitzar_pantalla()

def actualitzar_cooldowns():    # cooldowns 
    for p in powerups.values():
        if p["cooldown"] > 0:
            p["cooldown"] -= 1
    actualitzar_pantalla()
    finestra.after(1000, actualitzar_cooldowns)


def activar_radio():
    global cookies, cooldown_radio, radio_actiu
    global valor_clic, valor_clic_original
    if cooldown_radio > 0:
        return
    cookies += 1_000_000    # dona 1M de cookies
    cooldown_radio = 300    # cooldowns de 5 minuts
    radio_actiu = 60    # durada 1 minut
    valor_clic_original = valor_clic    # guarda valor original
    valor_clic *= 5 # multiplica els clics x5
    canvas_cookie.itemconfig(canvas_cookie.image_id, image=cookie_radio)
    canvas_cookie.image = cookie_radio
    actualitzar_pantalla()

# bucle per controlar el temps del mode radioactiu
def loop_radio():
    global cooldown_radio, radio_actiu, valor_clic
    if cooldown_radio > 0:
        cooldown_radio -= 1
    if radio_actiu > 0:
        radio_actiu -= 1
        if radio_actiu == 0:    # quan s'acaba el temps
            canvas_cookie.itemconfig(canvas_cookie.image_id, image=cookie_normal)   # torna la cookie normal
            canvas_cookie.image = cookie_normal
            valor_clic = valor_clic_original    # torna el valor del click normal
    if cookies >= 20000 and boto_radio is None: # apareix el botó per 1r cop als 20k
        crear_boto_radio()
    finestra.after(1000, loop_radio)

def crear_boto_radio(): # crear el mode radioactiu
    global boto_radio
    boto_radio = tk.Button(
        finestra,
        text="MODE RADIOACTIU",
        bg="#39FF14",
        fg="black",
        width=25,
        command=activar_radio
    )
    boto_radio.grid(row=3, column=0, pady=10)

# actualitzar interficie com textos i estats
def actualitzar_pantalla():
    etiqueta_cookies.config(text="Cookies: " + format_num(cookies))
    etiqueta_cps.config(text="Cookies/s: " + format_num(cookies_seg))
    for nom, item in compres.items():   # actualitza botons d'edificis
        botons[nom].config(
            text=f"{nom}\nPreu: {format_num(item['preu'])}\nQuantitat: {format_num(item['quantitat'])}",    # si no tens suficients cookies el botó es veu gris com desactivat
            bg=colors_compres[nom] if cookies >= item["preu"] else "SystemButtonFace"
        )

    # actualitza botons de powerups
    for nom, p in powerups.items():
        boto = {
            "click": boto_powerup_click,
            "avies": boto_powerup_avies,
            "granja": boto_powerup_granja
        }[nom]

        if p["cooldown"] > 0:
            boto.config(text=f"Powerup {nom.capitalize()} x2\nCooldown: {p['cooldown']}s")
        else:
            boto.config(text=f"Powerup {nom.capitalize()} x2\nPreu: {format_num(p['preu'])}")

    # actualitza el botó radioactiu
    if boto_radio:
        boto_radio.config(
            text=f"MODE RADIOACTIU\nCooldown: {cooldown_radio}s" if cooldown_radio > 0 else "MODE RADIOACTIU",
            state="disabled" if cooldown_radio > 0 else "normal"
        )

# funció iniciar 
def iniciar(f, ec, eps, b, b_click, b_avies, b_granja, canvas, img_normal, img_radio):
    global finestra, etiqueta_cookies, etiqueta_cps
    global botons
    global boto_powerup_click, boto_powerup_avies, boto_powerup_granja
    global canvas_cookie, cookie_normal, cookie_radio

    finestra = f
    etiqueta_cookies = ec
    etiqueta_cps = eps
    botons = b
    boto_powerup_click = b_click
    boto_powerup_avies = b_avies
    boto_powerup_granja = b_granja
    canvas_cookie = canvas
    cookie_normal = img_normal
    cookie_radio = img_radio

    auto_sum()  # iniciar el loop de cookies
    actualitzar_cooldowns() # iniciar el de cooldowns
    loop_radio()    # iniciar el de radioactiiu