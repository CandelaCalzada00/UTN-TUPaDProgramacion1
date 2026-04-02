# Este programa es una simulación de agenda de turnos.
# a- Ingresas tu nombre de operador
# b- Visualizarás un menú con 5 opciones:
#   1. Reservar turno       --> Tendras disponible 4 turnos para lunes y 3 para martes  --> En caso de estar disponible, se agendará. Pero, si la persona ya está agendada para ese día, no podrás hacerlo nuevamente.
#   2. Cancelar turno       --> Podrás cancelar el turno de un paciente ingresando su nombre --> En caso que no exista, no podrás hacerlo.
#   3. Ver agenda del día   --> Se imprimirán los turnos libres y los ya agendados con los nombres de los pacientes.
#   4. Ver resumen gral     --> Verás las agendas de ambos días y cual es el que tiene más carga o si tienen la misma.
#   5. Cerrar sistema       --> Saldrás del sistema


print("\n----------")
print("Ejercicio 3 — Agenda de Turnos con Nombres (sin listas)")
print("----------\n")

att_lunes = 4
att_martes = 3
paciente = ""

paciente_lunes_1 = ""
paciente_lunes_2 = ""
paciente_lunes_3 = ""
paciente_lunes_4 = ""

paciente_martes_1 = ""
paciente_martes_2 = ""
paciente_martes_3 = ""

while True:
    operador = input("Ingresá el nombre del operador: ").capitalize()
    print("")
    
    # Verifica que solo tenga letras:
    if not operador.isalpha():
        print("xxxxxxxxxx")
        print("🚩 ERROR: El nombre solo debe contener letras.")
        print("xxxxxxxxxx\n")
        continue # Si no cumple, vuelve a pedir
    break
    
# Menú repetitivo:
while True:
            opcion = input("Ingresá una opción:\n" \
            " 1- Reservar turno \n" \
            " 2- Cancelar turno \n" \
            " 3- Ver agenda del día \n" \
            " 4- Ver resumen general \n" \
            " 5- Cerrar sistema \n\n " \
            "👉 Opción elegida: ")
            print("")

            # validar que la opción ingresada sea un digito
            if not opcion.isdigit():
                print("xxxxxxxxxx")
                print("🚩 ERROR: Ingresá una opción numérica.")
                print("xxxxxxxxxx\n")
                continue # Si no cumple, vuelvo al menú

            opcion = int(opcion) # Convierto en int para trabajarla

            # validar que la opción ingresada sea del 1 al 5:
            if opcion < 1 or opcion > 5:
                print("xxxxxxxxxx")
                print("🚩 ERROR: Opción fuera de rango.")
                print("xxxxxxxxxx\n")
                continue # Si no cumple, vuelvo al menú
            

            # INICIO OPCIÓN 1 - CARGAR TURNO
            if opcion == 1:
                print("💾 RESERVACIÓN DE TURNOS: \n")
                
                while True:# BUCLE PARA NO VOLVER AL MENU PRINCIPAL

                    turno_dia = input("Elegí un día: \n " \
                    " 1- Lunes \n " \
                    " 2- Martes \n\n " \
                    "👉 Día: ")
                    print("")

                    #  si escribe letras:
                    if not turno_dia.isdigit():
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Ingresá una opción numérica.")
                        print("xxxxxxxxxx\n")
                        continue # Si no cumple, vuelve a pedir día

                    turno_dia = int(turno_dia) # lo convierto en int para trabajarlo

                    #  Si escribe número fuera de rango:
                    if turno_dia != 1 and turno_dia != 2:
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Opción fuera de rango.")
                        print("xxxxxxxxxx\n")
                        continue   # vuelve a pedir día

                    break # Sale del while cuando se ingresa bien el día (1 o 2)
                    
                # INICIO DÍA 1 --> LUNES:
                if turno_dia == 1:

                    while att_lunes > 0: # Si hay turnos libres entro al while
                        
                        print(f"🏥 Para el lunes hay {att_lunes} turnos disponibles.")
                        consulta_lunes = input("    ¿Querés reservar uno? (Si/No): ").upper()
                        print("")

                        # Si quiero reservar turno:
                        if consulta_lunes == "SI":

                            while True: #pido ingresar el paciente hasta que se ponga bien
                                paciente = input("      😷 Ingresá el nombre del paciente: ").capitalize()

                                # Verifico que el nombre sean solo letras
                                if not paciente.isalpha():
                                    print("\nxxxxxxxxxx")
                                    print("🚩 ERROR: El nombre solo puede contener letras.")
                                    print("xxxxxxxxxx\n")
                                    continue # vuelve a pedir el nombre
                                
                                break #salgo del while cuando ponga bien el nombre del paciente

                            

                            # VALIDACIÓN DE PACIENTE REPTIDO: comparo si paciente coincide con alguno ya guardado
                            if (paciente == paciente_lunes_1 or
                                paciente == paciente_lunes_2 or
                                paciente == paciente_lunes_3 or
                                paciente == paciente_lunes_4):
                                
                                print("\nxxxxxxxxxx")
                                print("🚩 ERROR: El paciente ya tiene reservado un turno para el lunes.")
                                print("xxxxxxxxxx\n")
                                continue

                            # SI EL PACIENTE NO ES REPETIDO, agendo turno en variable libre:
                            if paciente_lunes_1 == "":
                                paciente_lunes_1 = paciente
                                print(f"        --> ✅ Turno 1 del lunes reservado a {paciente_lunes_1}")
                                print("\n----------\n")
                                att_lunes -=1

                            elif paciente_lunes_2 == "":
                                paciente_lunes_2 = paciente
                                print(f"        --> ✅ Turno 2 del lunes reservado a {paciente_lunes_2}")
                                print("\n----------\n")
                                att_lunes -=1

                            elif paciente_lunes_3 == "":
                                paciente_lunes_3 = paciente
                                print(f"        --> ✅ Turno 3 del lunes reservado a {paciente_lunes_3}")
                                print("\n----------\n")
                                att_lunes -=1

                            elif paciente_lunes_4 == "":
                                paciente_lunes_4 = paciente
                                print(f"        --> ✅ Turno 4 del lunes reservado a {paciente_lunes_4}")
                                att_lunes -=1
                        
                        # Si indicas que no no queres turno:
                        elif consulta_lunes == "NO":
                            print("         --> ❌ No se ha reservado turno para el lunes.")
                            print("----------\n")
                            break #termino el while

                        else: #si indicas algo distinto a Si o No:
                            print("xxxxxxxxxx")
                            print("🚩 ERROR: Opción inválida.")
                            print("xxxxxxxxxx\n")
                        
                    else: # Si no hay más turnos para el lunes
                        print("\nxxxxxxxxxx")
                        print("🗳️ Todos los turnos del lunes están reservados.")
                        print("xxxxxxxxxx\n")
                # FIN DE DÍA 1 --> LUNES

                # INICIO DE DÍA 2 --> MARTES
                elif turno_dia == 2:

                    while att_martes != 0: #Si hay turnos, entro al while
                        
                        print(f"🏥 Para el martes hay {att_martes} turnos disponibles.")
                        consulta_martes = input("   ¿Querés reservar uno? (Si/No): ").upper()
                        print("")

                        # Si quiero reservar turno:
                        if consulta_martes == "SI":

                            while True: #pido ingresar el paciente hasta que se ponga bien
                                paciente = input("      😷 Ingresá el nombre del paciente: ").capitalize()

                                # Verifico que el nombre sean solo letras
                                if not paciente.isalpha():
                                    print("\nxxxxxxxxxx")
                                    print("🚩 ERROR: El nombre solo puede contener letras.")
                                    print("xxxxxxxxxx\n")
                                    continue # vuelve a pedir el nombre
                                
                                break #salgo del while cuando ponga bien el nombre del paciente


                            # VALIDACIÓN DE PACIENTE REPTIDO: comparo si paciente coincide con alguno ya guardado
                            if (paciente == paciente_martes_1 or
                                paciente == paciente_martes_2 or
                                paciente == paciente_martes_3):
                                
                                print("\nxxxxxxxxxx")
                                print("🚩 ERROR: El paciente ya tiene reservado un turno para el martes.")
                                print("xxxxxxxxxx\n")
                                continue

                            # SI EL PACIENTE NO ES REPETIDO, agendo turno en variable libre:
                            if paciente_martes_1 == "":
                                paciente_martes_1 = paciente
                                print(f"        --> ✅ Turno 1 del martes asignado a {paciente_martes_1}")
                                print("\n----------\n")
                                att_martes -=1

                            elif paciente_martes_2 == "":
                                paciente_martes_2 = paciente
                                print(f"        --> ✅ Turno 2 del martes asignado a {paciente_martes_2}")
                                print("\n----------\n")
                                att_martes -=1

                            elif paciente_martes_3 == "":
                                paciente_martes_3 = paciente
                                print(f"        --> ✅ Turno 3 del martes asignado a {paciente_martes_3}")
                                att_martes -=1

                        # Si indicas que no queres turno:
                        elif consulta_martes == "NO":
                            print("         --> ❌ No se ha reservado turno para el martes.")
                            print("----------\n")
                            break #termino el while

                        else: #si indicas algo distinto a Si o No:
                            print("xxxxxxxxxx")
                            print("🚩 ERROR: Opción inválida.")
                            print("xxxxxxxxxx\n")

                        
                    else: # Si no hay más turnos para martes
                        print("\nxxxxxxxxxx")
                        print("🗳️ Todos los turnos del martes están reservados.")
                        print("xxxxxxxxxx\n")

                # FIN DE DÍA 2 --> MARTES
            # FIN OPCIÓN 1 - CARGAR TURNO

            # INICIO OPCIÓN 2 - CANCELAR TURNO
            elif opcion == 2:
                print("🚫 CANCELACIÓN DE TURNOS: \n")
                #INICIO Comprobación para que el día sea correcto
                while True:

                    turno_dia = input("Elija un día: \n" \
                    " 1- Lunes \n" \
                    " 2- Martes \n" \
                    "👉 Día: ")
                    print("")

                    #  si escribe letras
                    if not turno_dia.isdigit():
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Opción inválida.")
                        print("xxxxxxxxxx\n")
                        continue   # vuelve a pedir día

                    turno_dia = int(turno_dia)

                    #  número fuera de rango
                    if turno_dia != 1 and turno_dia != 2:
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Opción fuera de rango.")
                        print("xxxxxxxxxx\n")
                        continue   # vuelve a pedir día

                    break # Sale del while cuando se ingresa bien el día (1 o 2)


                # INICIO DIA 1 --> LUNES
                if turno_dia == 1:

                    # Verifico si NO hay pacientes cargados el lunes
                    if (paciente_lunes_1 == "" and
                        paciente_lunes_2 == "" and
                        paciente_lunes_3 == "" and
                        paciente_lunes_4 == ""):

                        print("xxxxxxxxxx")
                        print("--> ❌ No hay pacientes cargados para el lunes.")
                        print("xxxxxxxxxx\n")

                        continue   # vuelve al menú principal

                    # INICIO Comprobación de nombre paciente
                    while True:
                        paciente = input("  😷 Ingresá el nombre del paciente para cancelar su turno del lunes: ").capitalize()

                        if not paciente.isalpha():
                            print("\nxxxxxxxxxx")
                            print("🚩 ERROR: El nombre solo puede contener letras.")
                            print("xxxxxxxxxx\n")
                            continue # vuelve a pedir el nombre

                        #Compruebo que el paciente ingresado coincida con los cargados antes:
                        if (paciente != paciente_lunes_1 and
                            paciente != paciente_lunes_2 and
                            paciente != paciente_lunes_3 and
                            paciente != paciente_lunes_4):
                            
                            print("\nxxxxxxxxxx")
                            print("🚩 ERROR: El paciente ingresado no tiene turno para el lunes.")
                            print("xxxxxxxxxx\n")
                            continue
                        
                        break #salgo del while cuando ponga bien el nombre del paciente
                    # FIN Comprobación de nombre paciente


                    # INICIO Si encuentra al paciente, se borra:
                    if paciente == paciente_lunes_1:
                        paciente_lunes_1 = ""
                        print("         --> ✅ Se ha borrado el turno 1 correctamente")
                        print("\n----------\n")
                        att_lunes +=1
                    
                    elif paciente == paciente_lunes_2:
                        paciente_lunes_2 = ""
                        print("         --> ✅ Se ha borrado el turno 2 correctamente")
                        print("\n----------\n")
                        att_lunes +=1
                    
                    elif paciente == paciente_lunes_3:
                        paciente_lunes_3 = ""
                        print("         --> ✅ Se ha borrado el turno 3 correctamente")
                        print("\n----------\n")
                        att_lunes +=1
                    
                    elif paciente == paciente_lunes_4:
                        paciente_lunes_4 = ""
                        print("         --> ✅ Se ha borrado el turno 4 correctamente")
                        print("\n----------\n")
                        att_lunes +=1
                    # FIN Si encuentra al paciente, se borra
                # FIN DIA 1 --> LUNES

                # INICIO DIA 2 --> MARTES
                if turno_dia == 2:

                    # Verifico si NO hay pacientes cargados el martes
                    if (paciente_martes_1 == "" and
                        paciente_martes_2 == "" and
                        paciente_martes_3 == ""):

                        print("xxxxxxxxxx")
                        print("--> ❌ No hay pacientes cargados para el martes.")
                        print("xxxxxxxxxx\n")

                        continue # vuelve al menú principal

                    # INICIO Comprobación de nombre paciente
                    while True:
                        paciente = input("  😷 Ingresá el nombre del paciente para cancelar tu turno del martes: ").capitalize()

                        if not paciente.isalpha():
                            print("xxxxxxxxxx")
                            print("🚩 ERROR: El nombre solo puede contener letras.")
                            print("xxxxxxxxxx\n")
                            continue # vuelve a pedir el nombre

                        #Compruebo que el paciente ingresado coincida con los cargados antes:
                        if (paciente != paciente_martes_1 and
                            paciente != paciente_martes_2 and
                            paciente != paciente_martes_3):
                            
                            print("\nxxxxxxxxxx")
                            print("🚩 ERROR: El paciente ingresado no tiene turno para el martes.")
                            print("xxxxxxxxxx\n")
                            continue
                        
                        break #salgo del while cuando ponga bien el nombre del paciente
                    # FIN Comprobación de nombre paciente

                    # INICIO Si encuentra al paciente, se borra:
                    if paciente == paciente_martes_1:
                        paciente_martes_1 = ""
                        print("         --> ✅ Se ha borrado el turno 1 correctamente")
                        print("\n----------\n")
                        att_martes +=1
                    
                    elif paciente == paciente_martes_2:
                        paciente_martes_2 = ""
                        print("         --> ✅ Se ha borrado el turno 2 correctamente")
                        print("\n----------\n")
                        att_martes +=1
                    
                    elif paciente == paciente_martes_3:
                        paciente_martes_3 = ""
                        print("         --> ✅ Se ha borrado el turno 3 correctamente")
                        print("\n----------\n")
                        att_martes +=1
                    # FIN Si encuentra al paciente, se borra
                # FIN DIA 2 --> MARTES
            #FIN OPCIÓN 2 - CANCELAR TURNO

            # INICIO OPCIÓN 3 - AGENDA DEL DÍA
            elif opcion == 3:
                print("📅 AGENDA DEL DÍA: \n")

                while True:# BUCLE PARA NO VOLVER AL MENU PRINCIPAL

                    turno_dia = input("Elija un día: \n 1- Lunes \n 2- Martes \n Día: ")
                    print("")

                    #  si escribe letras
                    if not turno_dia.isdigit():
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Opción inválida.")
                        print("xxxxxxxxxx\n")
                        continue   # vuelve a pedir día

                    turno_dia = int(turno_dia)

                    #  número fuera de rango
                    if turno_dia != 1 and turno_dia != 2:
                        print("xxxxxxxxxx")
                        print("🚩 ERROR: Opción fuera de rango.")
                        print("xxxxxxxxxx\n")
                        continue   # vuelve a pedir día

                    break # Sale del while cuando se ingresa bien el día (1 o 2)

                # SI ELIJO 1 --> LUNES:
                if turno_dia == 1:
                    print("Turnos del lunes:")
                    # INICIO Listado de los turnos, si están asignados se muestra el paciente, sino libre:
                    if paciente_lunes_1 != "":
                        print(f"    - 📌 El turno 1 lo reservó {paciente_lunes_1}.")
                    else:
                        print("    - ✅ Turno 1 disponible.")
                    
                    if paciente_lunes_2 != "":
                        print(f"    - 📌 El turno 2 lo reservó {paciente_lunes_2}.")
                    else:
                        print("    - ✅ Turno 2 disponible.")
                    
                    if paciente_lunes_3 != "":
                        print(f"    - 📌 El turno 3 lo reservó {paciente_lunes_3}.")
                    else:
                        print("    - ✅ Turno 3 disponible.")
                    
                    if paciente_lunes_4 != "":
                        print(f"    - 📌 El turno 4 lo reservó {paciente_lunes_4}.")
                    else:
                        print("    - ✅ Turno 4 disponible.")
                    print("\n----------\n")
                    # FIN de listado de turnos lunes
                # FIN 1 --> LUNES

                #SI ELIJO 2 --> MARTES
                if turno_dia == 2:
                    print("Turnos del martes:")
                    # INICIO Listado de los turnos, si están asignados se muestra el paciente, sino libre:
                    if paciente_martes_1 != "":
                        print(f"    - 📌 El turno 1 lo reservó {paciente_martes_1}.")
                    else:
                        print("    - ✅ Turno 1 disponible.")
                    
                    if paciente_martes_2 != "":
                        print(f"    - 📌 El turno 2 lo reservó {paciente_martes_2}.")
                    else:
                        print("    - ✅ Turno 2 disponible.")
                    
                    if paciente_martes_3 != "":
                        print(f"    - 📌 El turno 3 lo reservó {paciente_martes_3}.")
                    else:
                        print("    - ✅ Turno 3 disponible.")
                    print("\n----------\n")
                    # FIN de listado de turnos martes
                # FIN 2 --> MARTES
            # FIN OPCIÓN 3 - AGENDA DEL DÍA


            # INICIO OPCIÓN 4 - RESUMEN GENERAL
            elif opcion == 4:
                print("RESUMEN GENERAL: \n")

                # INICIO Listado de los turnos LUNES
                print("Turnos del lunes:")
                if paciente_lunes_1 != "": #Si el turno está reservado, muestro el if, sino, su respectivo else
                    print(f"    - 📌 El turno 1 lo reservó {paciente_lunes_1}.")
                else:
                    print("    - ✅ Turno 1 disponible.")
                
                if paciente_lunes_2 != "":
                    print(f"    - 📌 El turno 2 lo reservó {paciente_lunes_2}.")
                else:
                    print("    - ✅ Turno 2 disponible.")
                
                if paciente_lunes_3 != "":
                    print(f"    - 📌 El turno 3 lo reservó {paciente_lunes_3}.")
                else:
                    print("    - ✅ Turno 3 disponible.")
                
                if paciente_lunes_4 != "":
                    print(f"    - 📌 El turno 4 lo reservó {paciente_lunes_4}.")
                else:
                    print("    - ✅ Turno 4 disponible.")
                print("")
                # FIN de listado de turnos lunes
                

                # INICIO Listado de los turnos MARTES
                print("Turnos del martes:")
                
                if paciente_martes_1 != "":
                    print(f"    - 📌 El turno 1 lo reservó {paciente_martes_1}.")
                else:
                    print("    - ✅ Turno 1 disponible.")
                
                if paciente_martes_2 != "":
                    print(f"    - 📌 El turno 2 lo reservó {paciente_martes_2}.")
                else:
                    print("    - ✅ Turno 2 disponible.")
                
                if paciente_martes_3 != "":
                    print(f"    - 📌 El turno 3 lo reservó {paciente_martes_3}.")
                else:
                    print("    - ✅ Turno 3 disponible.")
                print("")
                # FIN de listado de turnos martes

                # Para mostrar el resumen de turnos:
                ocupados_lunes = 4 - att_lunes # Para saber cuantos turnos se ocuparon
                ocupados_martes = 3 - att_martes # Para saber cuantos turnos se ocuparon

                print("☝️ En síntesis:")
                print(f"    - Lunes: {ocupados_lunes} turnos ocupados de 4")
                print(f"    - Martes: {ocupados_martes} turnos ocupados de 3")

                # Calculo el día con más turnos:
                if ocupados_lunes > ocupados_martes:
                    print("         --> El día con más turnos reservados es: Lunes")

                elif ocupados_martes > ocupados_lunes:
                    print("         --> El día con más turnos reservados es: Martes")

                elif ocupados_lunes == 0 and ocupados_martes == 0:
                    print("         --> Ningún día tiene turnos reservados.")
                else:
                    print("         --> Ambos días tienen la misma cantidad de turnos reservados.")

                print("\n----------\n")
            
            # FIN OPCIÓN 4 - RESUMEN GENERAL

            # INICIO OPCIÓN 3 - SALIR DEL SISTEMA
            elif opcion == 5:
                print("Saliendo del sistema 👋")
                print("\n-------\n")
                exit()
            # FIN OPCIÓN 3 - SALIR DEL SISTEMA