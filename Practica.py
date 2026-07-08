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


def search_key(key_search_input, array_dict):
    key_search_input.strip().upper()

    for array_key in array_dict.keys():
        if key_search_input == array_key:
            return True
    
    return False


def delete_key(key_search_input, array_dict, bodega_dict): #case 5

    if search_key(key_search_input, array_dict):

        del array_dict[key_search_input]
        del bodega_dict[key_search_input]

        return True
    
    else:
        return False


#==================================================|

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
            print("")

        case 4:
            print("")

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