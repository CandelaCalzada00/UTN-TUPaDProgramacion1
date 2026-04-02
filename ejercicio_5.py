# Este programa es un simulador de juego de Arena. Tu objetivo es matar a tu enemigo.
# Primero ingresarás tu nombre y verás un menú con acciones. Al final de cada acción, será turno de tu enemigo y te atacará.
#   1. Ataque pesado --> Infliges un golpe normal, pero si el enemigo tiene menos de 20HP, le darás un golpe crítico.
#   2. Ráfaga veloz  --> Lanzas 3 golpes seguidos de 5 de daño.
#   3. Curarse --> Consumes una poción y regeneras vida. En caso de no tener más, perdés el turno.
# Si lo matás, ganás... Sino, perdés.

print("\n----------")
print("Ejercicio 5 — Escape Room: La Arena del Gladiador")
print("----------\n")


# Variables iniciales:
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
dano_base = 15
dano_enemigo = 12
turno_gladiador = True

while True: #Entra al While y no sale hasta poner bien el nombre del gladiador:
            print("")
            nombre_gladiador = input("Ingresá tu nombre de gladiador: ").capitalize()
            print("\n................")
            
            if not nombre_gladiador.isalpha():
                print("\nxxxxxxxxxx")
                print("🚩 ERROR: Solo se permiten letras.")
                print("xxxxxxxxxx\n")
                continue
            break

while vida_gladiador > 0 and vida_enemigo > 0: #Si se cumple, el juego funciona
    


    # TURNO DEL GLADIADOR:
    if turno_gladiador == True:
        print("")
        print("=== NUEVO TURNO ===")
        print("")
        print(f"🦂 Gladiador {nombre_gladiador} (HP: {vida_gladiador}) VS 🐍 Enemigo (HP: {vida_enemigo}) | | 💊 Pociones: {pociones_vida} (+30 HP)")
        print("")

        # INICIO DE MENÚ DE COMBATE
        while True:
            
            print("> > Turno del gladiador < <")
            print("")
            accion_gladiador = input( 
            "Ingresá una acción:\n " \
            "1- ATAQUE PESADO   (15 de daño + probabilidad de crítico) \n " \
            "2- RÁFAGA VELOZ    (3 golpes de 5 de daño) \n " \
            "3- CURARSE         (consume poción)\n\n" \
            "Acción elegida: ")


            # validar que la acción sea un digito
            if not accion_gladiador.isdigit():
                print("xxxxxxxxxx")
                print("🚩 ERROR: Acción inválida.")
                print("xxxxxxxxxx\n")
                continue 

            accion_gladiador = int(accion_gladiador)

            # validar que la acción sea del 1 al 3
            if accion_gladiador < 1 or accion_gladiador > 3:
                print("xxxxxxxxxx")
                print("🚩 ERROR: Acción fuera de rango.")
                print("xxxxxxxxxx\n")
                continue

            break
        # --------------------------------------------------
        # --------------------------------------------------


        # INICIO ACCIÓN 1: ATAQUE PESADO
        if accion_gladiador == 1:

            # Si el enemigo tiene - de 20 HP, hago golpe critico: 
            if vida_enemigo < 20:
                dano_final = dano_base * 1.5  # Calculo cuanto es el golpe crítico
                print(f"     ¡Lanzaste un golpe crítico y provocaste {dano_final} ptos de daño! 💥")
            else:
                dano_final = dano_base
                print(f"     ¡Atacaste al enemigo por {dano_final} ptos de daño! 👊\n")

            vida_enemigo -= dano_final #Resto vida al enemigo

            if vida_enemigo <= 0: # Si luego de atacarlo, su vida es 0, ya termina el programa
                break

            turno_gladiador = False
        # FIN ACCIÓN 1: ATAQUE PESADO


        # INICIO ACCIÓN 2: RAFAGA VELOZ
        elif accion_gladiador == 2:
            for contador_golpes in range(3):
                vida_enemigo -= 5 #Resto vida al enemigo en cada vuelta
                print("     ¡Golpe conectado por 5 de daño! 💫")
            print("")
            print("         Le provocaste al enemigo 15 ptos de daño en total 😎\n")

            if vida_enemigo <= 0: # Si luego de atacarlo, su vida es 0, ya termina el programa
                break


            turno_gladiador = False
        # FIN ACCIÓN 2: RÁFAGA VELOZ


        # INICIO ACCIÓN 3: CURARSE
        elif accion_gladiador == 3:

            # Vida llena → NO pierde turno
            if vida_gladiador == 100:
                print("     No necesitas curarte, tienes el 100% de tu vida 😎\n")

            # Tiene pociones --> se cura y pasa turno
            elif pociones_vida > 0:
                pociones_vida -= 1 #Se consume 1
                vida_gladiador += 30

                # Si al curar la vida sube de 100, la limito:
                if vida_gladiador > 100:
                    vida_gladiador = 100

                print("     ¡Has recuperado 30 ptos de HP! 🩹\n")
                
                turno_gladiador = False

            # No hay pociones --> pierde turno
            else:
                print("     ¡No quedan pociones! 💊\n")
                turno_gladiador = False
        #FIN ACCIÓN 3: CURARSE


    # TURNO DEL ENEMIGO
    else:
        print("x x x x x x x x x")
        print("> > Turno del enemigo < <")
        vida_gladiador -= dano_enemigo
        print(f"    ¡El enemigo te atacó por {dano_enemigo} puntos de daño! ⚔️")
        turno_gladiador = True
        print("x x x x x x x x x")


else:
    if vida_enemigo <= 0:
        print(f"\n🏆 ¡VICTORIA! {nombre_gladiador}, ha ganado la batalla. 🏆\n")
    else:
        print(f"\n☠️  ¡DERROTA! {nombre_gladiador}, has caído en combate. ☠️\n")