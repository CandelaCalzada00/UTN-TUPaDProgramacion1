# Este programa es una simulación de un juego de escape de una bóveda Tu objetivo es abrir las 3 cerraduras antes de quedarte sin tiempo/energía o bloquear por alarma
# Primero ingresarás tu nombre de agente 
# Tendrás que elegir una acción del menú:
#   1. Forzar cerradura --> Abrirás un candado, pero no puedes repetirlo más de 2 veces, ya que se activará la alarma y no podrás forzar de nuevo. Además, si tienes menos de 40 de energía, estarás en Alerta de alarma, donde tendrás posibilidades de activarla si ingresas mal el nro.
#       *** Para poder forzar sin activar la alarma, debes elegir otra de las acciones y luego intentar nuevamente
#   2. Hackear el panel --> En la 1ra vez tendrás una mitad del código. En la 2da lo desbloquearás por completo y abrirás una cerradura. No tiene límite de intentos
#   3. Descansar        --> Recuperas energía, en caso de estar la alarma activa, recuperas menos.

# Si te quedás sin recursos o haces un bloqueo por alarma (si activas la alarma y el tiempo es menor/igual a 3), perdés.
# Si abrís las 3 cerraduras antes de perder recursos o bloquear la alarma, ganás.




print("\n----------")
print("Ejercicio 4 — Escape Room: La Bóveda")
print("----------\n")

# Variables iniciales (no se piden por teclado)
energia = 50
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

contador_forzar = 0

print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. \nSi abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.")

while True: #Entra al While y no sale hasta poner bien el nombre del agente:
    print("")
    nombre_agente = input("Ingresá tu nombre de agente: ").capitalize()
    print("")
    
    if not nombre_agente.isalpha():
        print("\nxxxxxxxxxx")
        print("🚩 ERROR: El nombre solo puede contener letras.")
        print("xxxxxxxxxx\n")
        continue
    break


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3: #El juego funciona si energía/tiempo es superior a cero y todas las cerraduras no han sido abiertas

    print("........\n")
    print(f"😎 Agente {nombre_agente}, tus parámetros son:\n - Energía = {energia} |- Tiempo = {tiempo} | - Cerradudas abiertas = {cerraduras_abiertas} / 3 \n")


    # INICIO DE MENÚ AGENTE
    while True:
        accion_agente = input( 
        "Ingresá una acción:\n " \
        "1- FORZAR CERRADURA    (costo: -20 energía, -2 tiempo) \n " \
        "2- HACKEAR PANEL       (costo: -10 energía, -3 tiempo) \n " \
        "3- DESCANSAR           (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)\n\n" \
        "Opción elegida: ")

        print("")

        # validar que la acción ingresada sea un digito
        if not accion_agente.isdigit():
            print("xxxxxxxxxx")
            print("🚩 ERROR: Acción inválida.")
            print("xxxxxxxxxx\n")
            continue 

        accion_agente = int(accion_agente)

        # validar que la acción ingresada sea del 1 al 3
        if accion_agente < 1 or accion_agente > 3:
            print("xxxxxxxxxx")
            print("🚩 ERROR: Acción fuera de rango.")
            print("xxxxxxxxxx\n")
            continue

        break #Si la acción está bien, se termina el bucle

    # --------------------------------------------------
    # --------------------------------------------------

    #INICIO ACCIÓN 1 --> FORZAR CERRADURA
    if accion_agente == 1:
        contador_forzar +=1

        if energia < 20:
            print("xxxxxxxxxx")
            print("¡No te alcanza la energía para forzar! 😴")
            print("xxxxxxxxxx\n")
            continue

        elif tiempo < 2:
            print("xxxxxxxxxx")
            print("¡No te alcanza el tiempo para forzar! ⌛")
            print("xxxxxxxxxx\n")
            continue

        elif contador_forzar < 3 and alarma == False:  #Si no se hacen 3 intentos seguidos
            if energia >= 40: #Si la energia es mayor a 40
                cerraduras_abiertas +=1 #Consiguió abrir una de las cerraduras
                print("¡Genial! Has abierto una cerradura 🎊")

            elif energia < 40:
                print("\nxxxxxxxxxx")
                print("¡Cuidado! Hay riesgo de alarma ⚠️")
                print("xxxxxxxxxx\n")

                # bucle para que se ponga opción del 1-3 + verificación:
                while True:
                    prueba_alarma = input("Ingresá un número del 1 al 3 para evitarla: ")
                    print("")

                    # validar que la opción ingresada sea un nro
                    if not prueba_alarma.isdigit():
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Acción inválida.")
                        print("xxxxxxxxxx\n")
                        continue 

                    prueba_alarma = int(prueba_alarma)

                    # validar que la opción ingresada sea del 1 al 3
                    if prueba_alarma < 1 or prueba_alarma > 3:
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Acción fuera de rango.")
                        print("xxxxxxxxxx\n")
                        continue
                    break

                if prueba_alarma != 3: #Si el nro ingresado es distinto de 3
                    cerraduras_abiertas +=1 #Consiguió abrir una de las cerraduras
                    print("¡Excelente! Has evitado la alarma y abriste una cerradura 👏")
                    
                    # Si bien aún hay tiempo/energía, el problema es que cuando se reste, quedarán en cero
                    if energia == 20 and cerraduras_abiertas !=3:
                        print("Pero... ¡Te has quedado sin energía! 😴")
                        print("")
                    if tiempo == 2 and cerraduras_abiertas !=3:
                        print("¡Pero te quedaste sin tiempo! 😥")
                        print("")

                else: #Si el nro es 3:
                    alarma = True
                    print("¡Oh no! Activó alarma 🚨")

                    # Si bien aún hay tiempo/energía, el problema es que cuando se reste, quedarán en cero
                    if energia == 20:
                        print("Y además, ¡Te has quedado sin enegía! 😴")
                        print("")
                    if tiempo == 2:
                        print("Y te has quedado sin tiempo 😥")
                        print("")
            
            #La acción resta:
            energia -= 20
            tiempo -=2

        elif alarma == True:
            print("No podés forzar porque la alarma está activada 🚨")
            print("")
            
            # Por mas que no logré nada, la acción resta:
            energia -= 20
            tiempo -=2


        elif contador_forzar >= 3: #Si intentas hacer la acción forzar 3 veces seguidas
            alarma = True
            print("Has forzado tantas veces seguidas, que activaste la alarma 🚨")
            

            # Si bien aún hay tiempo/energía, el problema es que cuando se reste, quedarán en cero
            if energia == 20:
                print("Y además, ¡Te has quedado sin enegía! 😴")
                print("")
            if tiempo == 2:
                print("Y te has quedado sin tiempo 😥")
                print("")

            # Por mas que no logré nada, la acción resta:
            energia -= 20
            tiempo -=2
    #FIN ACCIÓN 1 --> FORZAR CERRADURA

    #INICIO ACCIÓN 2 --> HACKEAR PANEL
    elif accion_agente == 2:

        if energia < 10:
            print("\nxxxxxxxxxx")
            print("¡No te alcanza la energía para hackear! 😴")
            print("xxxxxxxxxx\n")
            continue

        elif tiempo <3:
            print("\nxxxxxxxxxx")
            print("¡No te alcanza el tiempo para hackear!⌛")
            print("xxxxxxxxxx\n")
            continue
            
        elif cerraduras_abiertas < 3: 
            for cont in range(4): #El for suma un total de 4 A al ejecutarse.
                codigo_parcial += "A"
                print(codigo_parcial)
            
            if len(codigo_parcial) == 4: #Si el cód. tiene 4 caracteres:
                print("¡Has hackeado la mitad del código! 🖥️")
                
                # Si bien aún hay tiempo/energía, el problema es que cuando se reste, quedarán en cero
                if energia == 10:
                    print("Pero te has quedado a medio camino porque no tenés energía 😴")
                    print("")
                
                if tiempo == 3:
                    print("Lo ibas a lograr, pero te quedaste sin tiempo 😥")
                    print("")

            if len(codigo_parcial) >= 8: # Si el cód. tiene 8 o + caracteres:
                cerraduras_abiertas +=1 # Consiguió abrir una de las cerraduras
                codigo_parcial = "" # Si desbloqueo el código por completo, la próxima vez que ejecute la acción, estará restablecido para comenzar de cero
                
                print("¡Has hackeado todo el código y desbloqueado una cerradura! 🔓")
                
                # Si bien aún hay tiempo/energía, el problema es que cuando se reste, quedarán en cero
                if energia == 10 and cerraduras_abiertas !=3:
                    print("Execelente técnica, pero te has quedado sin enegía para continuar 😴")
                    print("")
                
                if tiempo == 3 and cerraduras_abiertas !=3:
                    print("¡Sos un maestro! Pero olvidaste lo más importante... El tiempo 😥")
                    print("")

            #La acción resta:
            energia -= 10
            tiempo -= 3
            if contador_forzar >= 1: # restablezco el contador de la acción 1 para poder forzar sin que suene la alarma
                contador_forzar = 0
    #FIN ACCIÓN 2 --> HACKEAR PANEL

    #INICIO ACCIÓN 3 --> DESCANSAR
    elif accion_agente == 3: 

        if alarma == True:
            energia +=5 # Si alarma encencida, carga 5 de energía
            print("Recuperaste poca energía porque la alarma está activada 🚩")

            # Si bien aún hay tiempo, el problema es que cuando se reste, quedará en cero
            if tiempo == 1:
                print("Y sumándole... Te quedaste sin tiempo 😥")
                print("")
        else:
            energia += 15 # Si alarma apagada, carga 15
            print("Has recuperado bastante energía ⚡")

            # Si bien aún hay tiempo, el problema es que cuando se reste, quedará en cero
            if tiempo == 1:
                print("Pero el tiempo se te ha terminado 😥")
                print("")

        if energia > 100: # Si al sumar energía, es más de 100. Se limita a 100 máx
            energia = 100

        
        #La acción resta:
        tiempo -= 1
        if contador_forzar >= 1: # restablezco el contador de la acción 1 para poder forzar sin que suene la alarma
            contador_forzar = 0
    #FIN ACCIÓN 3 --> DESCANSAR


    #INICIO ALARMA
    # CORTE POR ALARMAS
    if alarma == True and tiempo <= 3:
        break

    #FIN ALARMA



    # FIN DE MENÚ AGENTE

print("\n........\n")

# Si abriste las cerraduras:
if cerraduras_abiertas == 3:
    print(f"VICTORIA: Felicidades agente {nombre_agente}, has completado tu misión 🏆")
    print("")

#Si no tenes energía ni tiempo:
elif energia <= 0 or tiempo <= 0:
    print(f"DERROTA: Agente {nombre_agente}, te has quedado sin recursos y falló tu misión 😞")
    print("")

#Si no tenes energia/tiempo y encima activas 3 alarmas:
elif tiempo <= 3 and alarma == True:
    print(f"DERROTA: Agente {nombre_agente}, te has quedado sin tiempo y la alarma bloqueó el sistema...\nHas fallado rotundamente tu misión 😰")
    print("")