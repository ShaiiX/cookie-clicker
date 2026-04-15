# 🍪Cookie Clicker🍪

## Game Explanation

## Program Structure
The project is divided into two main files:
- A **main file** that contains the main program logic
- A **functions file** that contains all supporting functions

I imported the **Tkinter library** for the graphical interface, and the **PIL (Python Imaging Library)** to handle images using `Image` and `ImageTk`.

---

## Cookie Management
The game is based on cookie variables, including:
- Total cookies
- Cookies per second (CPS)
- Click value

Main functions:
- `clicar()` → manually adds cookies per click
- `auto_sum()` → automatically generates cookies per second

---

## Graphical Interface
Using Tkinter, I implemented:
- **Labels** to display total cookies and cookies per second
- A **Canvas** to display the cookie image
- **Buttons** for purchases and power-ups

I also created the function:
- `actualitzar_pantalla()` → updates all text elements, changes button colors depending on whether purchases are possible, and displays active cooldowns

---

## Large Number Formatting
The function `format_num(num)` formats large numbers:
- From 1,000 → displayed as “K” (thousands)
- From 1,000,000 → displayed as “M” (millions)

---

## Purchase System
The game includes buildings that generate cookies per second.

Each item has:
- Price
- CPS (cookies per second production)
- Quantity owned

The function:
- `comprar(nom)` → checks if the player has enough cookies, subtracts the cost, increases quantity, and increases the price by 15% after each purchase

---

## Power-Ups
Power-ups double production (x2).

Each power-up includes:
- Name
- Price
- Cooldown

Each purchase:
- Increases price by 50%
- Has a cooldown of 60 seconds

A single function manages power-ups:
- `millorar(nom)`

---

## Cooldowns
The function:
- `actualitzar_cooldowns()` decreases cooldown timers every second, updates the interface, and runs using `window.after(1000, ...)`

---

## Extra Features
- Button colors change depending on affordability (enough cookies or not)
- Cooldown system displays remaining time and prevents immediate reuse
- Increasing prices: +15% for buildings, +50% for power-ups
- Cookie image loaded using PIL and displayed on a Canvas

---

## Radioactive Cookie (Easter Egg)
A special easter egg activates when the player reaches **20,000 cookies**.

### Activation
- Function `activar_radio()` grants **1,000,000 cookies**
- Starts a **300-second cooldown**
- Activates a **60-second radioactive mode**

### Effects
During radioactive mode:
- Click power is multiplied by x5 temporarily
- The cookie image changes to a radioactive version using PIL and Canvas

### After Effect
- The cookie returns to its normal image
- Click power is restored to its previous value
- The button becomes inactive during cooldown and shows remaining time
