#===========================================================================|
#git config --global user.name/.mail "_"
#git clone [URL]
#cd [file]
#git add .
#git commit -m "_"
#git push origin master
#===========================================================================|

#Main Funciones de logica:==============================|
def read_menu():
    while True:
        print("""
===Menu===
1. Unidades por tipo
2. Busquedas de arreglo por rango
3. Actualizar Precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
""")
    
        try:
            option = int(input(">>>"))

            if option >= 1 and option <= 6:
                return option
            else:
                print("[Error] Please input a number within range (1-6).")

        except ValueError:
            print("[Error] Please input a number within range (1-6).")


def unidades_tipo(type_search, array_dict, bodega_dict): #case 1
    
    type_search = type_search.strip().lower() ## any "TEXT " is converted -> "text"
    quantity_arreglos = 0

    for array_key, array_value in array_dict.items():
        
        if type_search == array_value[1]: #Position in list is equal to [] + 1

            for bodega_key, bodega in bodega_dict.items():
                if array_key == bodega_key:
                    quantity_arreglos += bodega[1] 
                    break

    print(f"Quantity of arreglos available of type {type_search} is {quantity_arreglos}")


def price_search(price_min_range, price_max_range, array_dict, bodega_dict): #case 2

    array_list_range = []

    for bodega_key, bodega in bodega_dict.items():
        price = bodega[0] #Position in list is equal to [] + 1

        if price >= price_min_range and price <= price_max_range and bodega[1] > 0:

            for array_key, array_value in array_dict.items():

                if array_key == bodega_key:
                    
                    array_list_range.append(f"{array_value[0]} == {array_key}")
                    break

    if len(array_list_range) > 0:

        array_list_range.sort()

        for array_value in array_list_range:
            print(array_value)
    
    else:
        print("No items within price range.")


def price_update(key_search_input, change_new_price, array_dict, bodega_dict): #case 3

    if search_key(key_search_input, array_dict):

        bodega_dict[key_search_input][0] = change_new_price

        return True
    
    else:
        return False


def add_arreglo(val_input_code, val_input_name, val_input_type, 
                val_input_color, val_input_size, val_input_note, 
                val_input_season, val_input_price, val_input_amount, 
                array_dict, bodega_Dict): #case 4

    #In function
    if search_key(val_input_code, array_dict):
        return False
    else:
        array_dict[val_input_code] = [
            val_input_name,
            val_input_type,
            val_input_color,
            val_input_size,
            val_input_note,
            val_input_season
        ].append(array_dict)

        bodega_Dict[val_input_code] = [
            val_input_price,
            val_input_amount
        ]

        return True


def delete_key(key_search_input, array_dict, bodega_dict): #case 5

    if search_key(key_search_input, array_dict):

        del array_dict[key_search_input]
        del bodega_dict[key_search_input]

        return True
    
    else:
        return False

#Funcion de busqueda:===================================|
def search_key(key_search_input, array_dict):
    key_search_input.strip().upper()

    for array_key in array_dict.keys():
        if key_search_input == array_key:
            return True
    
    return False

#Funciones de Validacion:============================================|

def validacion_codigo(code_input_take): #not pre-existing, no empty spaces
    code_input_take = code_input_take.strip().upper()

    if len(code_input_take) == 0:
        return False

    else:
        return True

def validacion_nombre(name_input_take): #no empty spaces
    name_input_take = name_input_take.strip()

    if len(name_input_take) == 0:
        return False
    
    else:
        return True

def validacion_tipo(type_input_take): #no empty spaces
    type_input_take = type_input_take.strip().lower()

    if len(type_input_take) == 0:
        return False
    
    else:
        return True

def validacion_color_principal(color_input_take): #no empty spaces
    color_input_take = color_input_take.strip().lower()

    if len(color_input_take) == 0:
        return False
    
    else: 
        return True

def validacion_tamaño(size_input_take): #exactly 'S', 'M', 'L'
    size_input_take = size_input_take.strip().upper()

    if size_input_take not in ("S","M","L"):
        return False
    
    else:
        return True

def validacion_incluye_tarjeta(note_input_take): #input s or n, True if s, False if n
    note_input_take = note_input_take.strip().lower()

    if note_input_take == "s" or note_input_take == "n":
        return True
    else:
        return False

def validacion_temporada(season_input_take): #no empty spaces
    season_input_take = season_input_take.strip().lower()

    if len(season_input_take) == 0:
        return False
    
    else:
        return True

def validacion_precio(price_input_take): #int number > 0
    try:
        price_input_take = int(price_input_take)

        if price_input_take > 0:
            return True
        
        else:
            return False
    except ValueError:
        return False

def validacion_unidades(amount_input_take): #int number >= 0
    try:
        amount_input_take = int(amount_input_take)

        if amount_input_take >= 0:
            return True
        
        else:
            return False
    except ValueError:
        return False
#===================================================================|

#Codigo principal: =================================================|

#Constancias de inicio:

#Diccionario floral
arreglos = {
    'FL01': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FL02': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FL03': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FL04': ['Centro mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FL05': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FL06': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

#Diccionario de precios
bodega = {
    'FL01': [15990, 8],
    'FL02': [29990, 3],
    'FL03': [9990, 12],
    'FL04': [24990, 5],
    'FL05': [19990, 0],
    'FL06': [22990, 6],
}

#Si se quiere agregar un elemento a Arreglos a su vez se debe agregar a bodega (con sus elementos correctos.)

while True:
    option_select = read_menu()

    match option_select:
        case 1:
            type_input = input("Busqueda por tipo: ")

            unidades_tipo(type_input, arreglos, bodega) #Takes Arreglos and bodega as "_dict" due to position.
        
        case 2:
            try:
                min_range = int(input("Rango minimo: "))
                max_range = int(input("Rango maximo: "))

                if min_range < 0 or min_range > max_range:
                    print("[Error] Please input a valid minimum range.")
                
                else:
                    price_search(min_range, max_range, arreglos, bodega)

            except ValueError:
                print("[Error] Please input an interger value.")

        case 3:
            while True:
                try:
                    key_input = input("Porfavor ingrese el codigo a buscar: ")
                    new_price = int(input("Porfavor ingrese el nuevo precio: "))

                    if new_price <= 0:
                        print("El precio debe ser positivo.")
                        continue

                    
                    updated = price_update(key_input, new_price, arreglos, bodega)

                    if updated == True:
                        print("Price change was successful.")

                    else:
                        print("Key not found.")

                    again = input("¿Desea actualizar otro precio (s/n)? ").strip().lower()

                    if again == "n":
                        break    
                except ValueError:
                    print("[Error] Please input an interger value.")

        case 4:
            input_code = input("Ingrese el codigo: ")
            if not validacion_codigo(input_code):
                print("[Error]")
                continue
            
            input_name = input("Ingrese el nombre: ")
            if not validacion_nombre(input_name):
                print("[Error]")
                continue

            input_type = input("Ingrese el tipo de objeto: ")
            if not validacion_tipo(input_type):
                print("[Error]")
                continue

            input_color = input("Ingrese el color del objeto: ")
            if not validacion_color_principal(input_color):
                print("[Error]")
                continue

            input_size = input("Ingrese el tamaño del objeto (S/M/L): ")
            if not validacion_tamaño(input_size):
                print("[Error]")
                continue

            input_note = input("Ingrese si incluye tarjeta (s/n): ")
            if not validacion_incluye_tarjeta(input_note):
                print("[Error]")
                continue

            incluye_tarjeta = input_note.strip().lower() == "s"

            input_season = input("Ingrese la temporada del objeto: ")
            if not validacion_temporada(input_season):
                print("[Error]")
                continue

            input_price = input("Ingrese el valor de compra: ")
            if not validacion_precio(input_price):
                print("[Error]")
                continue

            input_amount = input("Ingrese la cantidad de unidades: ")
            if not validacion_unidades(input_amount):
                print("[Error]")
                continue

            #Else all:
            added = add_arreglo(input_code,
                        input_name, 
                        input_type, 
                        input_color, 
                        input_size, 
                        incluye_tarjeta, 
                        input_season, 
                        input_price, 
                        input_amount, 
                        arreglos, 
                        bodega
            )
            
            if added == True:
                print("Arreglo agregado con exito.")

            else:
                print("Codigo ya existente.")

        case 5:
            remove_key = input("Ingrese el codigo a eliminar: ")

            deleted = delete_key(remove_key, arreglos, bodega)

            if deleted == True:
                print("Key removal was successful.")

            else:
                print("Key not found.")

        case 6:
            print("Closing system...")
            break