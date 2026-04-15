README - Shaila Martínez
Explicacions del joc:

Estructura del programa: he dividit en 2 fitxers, un pel main on va el programa principal i l'altre
per a les funcions. 
He importat ls llibreries de tkinter per la interfície gràfica, també la
llibreria de PIL per poder posar imatges, he utilitzat el Image i Imagetk


Gestió de cookies:
Variable per les cookies, cookies per segon i valor del click. Funcio per sumar les galetes
manualment clicar() i suma automàticament les cookies per segon auto_sum().

Interfície gràfia:
Amn el tkinter he utilitzat label per mostrar les cookies totals i per seons, el canvas és per 
mostrar la imatge de la cookie, els buttons per compres i powerups. He utilitzat la funció 
actualitzar_pantalla() que actualitza els texts, canvia els colors segons si es pot comprar o no
i mostra els cooldowns actius

Format números grans:
Amb la funció format_num(num) per mostrar que a partir de 1000 es mostri una K de mil i a partir 
de 1000000 es mostri la M de millió.

Sistemes de compres:
Per comprar edificis que generen cookies/s. Cada element té preu, cps (clicks per segon) i quantitat
comprada. Amb la funció comprar(nom) comprova si hi ha prous cookies, resta el preu, aumenta la
quantitat i puja el preu un 15% cada vegada compratt
    
Powerups:
Fan una millora de la producció x2, he indicat la estructura amb el nom, el preu i un cooldown. 
Cada compra incrementa el preu un 50% i el seu cooldown es de 60 segons. He fet una única funció per 
aplicar el powerup: millorar(nom)

Coldowns:
Amb la funció actualitzar_cooldowns() el redueix cada segon, actualitza la pantalla i funciona amb
la finestra.after(1000, ..)

Opcions extres afegides:
- Colors segons la compra que es fa i si n'hi han suficients cookies
- Sistema de cooldown mostra els segons restants en pantalla i evita que el powerup es pugui
reutilitzar immediatament.
- Preus amb pujades, compres +15% cada vegada i powerups +50%.
- Imatge dela cookie utilitzant PIL per carregar la imatge i el canvas

Cookie radioactiva:
És un easteregg que apareix quan l’usuari té 20000 cookies, s'inicia el botó en mode reactiu que 
activa la cookie radioactiva.
Funcions i efectes: activar_radio() dona 1000000 cookies activa un cooldown de 300 segons i el mode 
radioactiu dura 60 segons. Durant aquest mode els clicks es multipliquen x5 temporalment i canvia la 
imatge de la cookie a la radioactiva amb PIL i canvas
Quan acaba el mode radioactiu la cookie torna a la imatge normal i els clics es restauren amb el 
valor que estaven abans. El botó mostra el cooldown que queda i es queda innactiu durant aquest temps.