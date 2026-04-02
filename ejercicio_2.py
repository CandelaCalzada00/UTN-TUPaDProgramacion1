# Este ejercicio es una simulación de acceso a un campus:
# Primero, se pide que se ingrese usuario y contraseña. Se tienen 3 intentos, en caso de fallar todos, la cuenta se bloquea.
# En caso que se ingrese, se presenta un menú con varias opciones:
#   1. Estado de inscripción    --> Verás el estado de tu inscripción.
#   2. Cambiar clave            --> Cambiarás tu clave, debe ser de mínimo 6 caracteres y tendrás que confirmarla.
#   3. Mensaje motivacional     --> Muestra un mensaje motivacional.
#   4. Salir

print("\n----------")
print("Ejercicio 2— Acceso al Campus y Menú Seguro")
print("----------\n")

usuario_correcto = "alumno"
clave_correcta = "python123"

for intento in range(1, 4):
    print(f"➡️  Intento {intento}/3")
    
    usuario = input("   Ingresá tu usuario: ")
    clave = input("   Ingresá tu clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("")
        print("Acceso concedido ✅\n")
        print("-----------------------\n")

        while True:
            opcion = input( 
            "Ingresá una opción:\n " \
            " 1- Estado de inscripción\n " \
            " 2- Cambiar clave\n " \
            " 3- Mensaje motivacional\n " \
            " 4- Salir\n\n " \
            "👉 Opción elegida: ")
            print("")

            # validar número
            if not opcion.isdigit():
                print("\nxxxxxxxxxx")
                print("🚩 ERROR: Ingresá un número válido.")
                print("\nxxxxxxxxxx\n")
                continue #vuelvo al principio del while

            opcion = int(opcion)

            # validar rango
            if opcion < 1 or opcion > 4:
                print("\nxxxxxxxxxx")
                print("🚩 ERROR: Opción fuera de rango.")
                print("\nxxxxxxxxxx\n")
                continue #vuelvo al principio del while

            #------------------------------------------
            # OPCIONES:
            #-----------------------------------------

            # INICIO OPCIÓN 1 --> Ver inscripción
            if opcion == 1:
                print(" ✅ Inscripto")
                print("\n-----------------------\n")
            # FIN OPCIÓN 1 --> Ver inscripción

            # INICIO OPCIÓN 2 --> Cambiar contraseña
            if opcion == 2:
                while True: #Si no pongo la contraseña y su confirmación bien, no salgo
                    clave_nueva = input("🔑 Ingresá una contraseña de mínimo 6 caracteres: ")
                    print("")

                
                    if len(clave_nueva) < 6: #Si clave tiene menos de 6
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Mínimo 6 caracteres.")
                        print("xxxxxxxxxx\n")
                        continue
                
                    else: #Si la contraseña tiene 6 o + carac...
                        confirmar = input("     --> Confirmá tu contraseña: ")
                        print("")

                        # Proceso de confirmación
                        while clave_nueva == confirmar:
                            clave_correcta = clave_nueva
                            print("         ✅ Clave actualizada")
                            print("\n-----------------------\n")
                            break
                        else: # Si no coinciden, pide de nuevo la contraseña
                            print("xxxxxxxxxx")
                            print("🚩 ERROR: Las claves no coinciden.")
                            print("xxxxxxxxxx\n")
                            continue #vuelvo al while anterior
                    break
            # FIN OPCIÓN 2 --> Cambiar contraseña       

            # INICIO OPCIÓN 3 --> Mensaje motivacional
            if opcion == 3:
                print("Tu esfuerzo de hoy, es el éxito de mañana. ✨")
                print("\n-----------------------\n")
            # FIN OPCIÓN 3 --> Mensaje motivacional

            if opcion == 4:
                print("Saliendo del Campus. 👋")
                print("\n-----------------------\n")
                exit()

    # SI LAS CREDENCIALES NO SON CORRECTAS:
    else:
        if intento < 3: # Si intenté menos de 3 veces...
            print("\nxxxxxxxxxx")
            print("🚩 ERROR: Credenciales inválidas.")
            print("xxxxxxxxxx\n")

        else: # Si intenté + de 2 veces...
            print("\nxxxxxxxxxx")
            print("Por exceso de intentos... Tu cuenta ha sido bloqueada. 🔒")
            print("xxxxxxxxxx\n")
            exit()