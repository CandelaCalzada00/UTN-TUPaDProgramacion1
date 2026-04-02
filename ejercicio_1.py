print("\n----------")
print("Ejercicio 1 — Caja del Kiosco")
print("----------\n")
# Este programa es una simulación de caja registradora:
# 1. Se carga el cliente y la cantidad de productos que comprará.
# 2. Se indica el costo de c/u y si tienen descuento.
#       --> En caso de descuento, se aplica un 10%OFF, sino, queda el costo original.
# 3. Al final se imprime por pantalla:
#   a. El total de los productos sin descuento.
#   b. El total de los productos con los descuentos aplicados.
#   c. Cuanto dinero se ahorró con los descuentos
#   d. Promedio por producto, es decir, cuanto saldrían si todos tuvieran el mismo precio.


total_sin_descuento = 0
total_con_descuento = 0
descuento_total = 0

# INICIO --> INGRESO EL NOMBRE DEL CLIENTE + VERIFICACIÓN:
cliente = input("Ingresá el nombre del cliente: ").capitalize()
print("")

while not cliente.isalpha(): # Si pones algo distinto a letras
    print("xxxxxxxxxx")
    print("🚩 ERROR: El nombre ingresado debe contener solo letras.")
    print("xxxxxxxxxx\n")

    cliente = input("Ingresá nuevamente el nombre del cliente: ").capitalize() # Pido nuevamente el nombre
    print("")
# FIN --> INGRESO EL NOMBRE DEL CLIENTE + VERIFICACIÓN


# INICIO --> INGRESO LA CANTIDAD DE PRODUCTOS + VERIFICACIÓN:
productos = input("🛒 Cantidad de productos: ")
print("")

while (not productos.isdigit()) or (int(productos) <= 0): # Si productos no es nro o menor a 0
    print("xxxxxxxxxx")
    print("🚩 ERROR: La cantidad de productos debe ser numérica y mayor a 0.")
    print("xxxxxxxxxx\n")

    productos = input("Ingresá nuevamente la cantidad de productos: ") #Ingreso nuevamente el producto
    print("")
# FIN --> INGRESO LA CANTIDAD DE PRODUCTOS + VERIFICACIÓN

productos = int(productos) # Convierto el producto a int para poder trabajarlo

# INICIO --> Bucle de cantidad de productos
for contador_productos in range(1, productos+1):
    precio = input(f"Ingresá el precio del producto {contador_productos}: $")

    while not precio.isdigit(): #si el precio no es entero, entro al while
        print("\nxxxxxxxxxx")
        print("🚩 ERROR: El precio debe ser numérico.")
        print("xxxxxxxxxx\n")

        precio= input(f"Ingresá el precio del producto {contador_productos}: $")
    
    precio = int(precio) #Convierto el precio a int para poder trabajarlo

    #INICIO --> Descuento:
    descuento = input("🎫 ¿El producto tiene descuento? \n Indique: S (SI) ó N (NO): \n - ").upper()
    print("")

    while descuento != "S" and descuento != "N": #si ingreso algo distinto a S o N:
        print("xxxxxxxxxx")
        print("🚩 ERROR: Debés ingresar S o N.")
        print("xxxxxxxxxx\n")

        descuento = input("🎫 ¿El producto tiene descuento? (S / N): ").upper()
        print("")
    

    #Comprobación de descuento:
    if descuento == "S":
        descuento_monto = precio * 0.10
        #no guardo el precio con descuento, sino lo que no pagué
        #Ej: $100 --> pago $90, pero guardo $10 porque ese fue el descuento.
    else:
        descuento_monto = 0

    # Va dentro del for porque con cada vuelta se actualiza
    descuento_total += descuento_monto
    total_sin_descuento += precio

# FIN --> Bucle de cantidad de productos

# Una vez termina el for, prosigue con esto:
total_con_descuento = total_sin_descuento - descuento_total
promedio = total_con_descuento / productos

print("\n===== 🛍️  RESUMEN DE COMPRA 🛍️ =====")
print(f" - Cliente: {cliente}")
print(f" - Total sin descuentos: ${total_sin_descuento}")
print(f" - Total con descuentos: ${total_con_descuento}")
print(f" - Ahorro total: ${descuento_total}")
print(f" - Promedio por producto: ${promedio:.2f}")