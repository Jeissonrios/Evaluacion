#Jeisson Rios Henao y Howar Patiño Patiño

empleados = {}
opcion = ''
while opcion != '5':
    if opcion == '1':
        cc = input('Introduce c.c del cliente: ')
        nombre = input('Introduce el nombre del empleado: ')
        cliente = {'nombre':nombre}
        empleados[cc] = cliente
    if opcion == '2':
        print('Lista de clientes')
        for clave, valor in empleados.items():
            print(clave, valor['nombre'])
    if opcion == '3':
        cc = input('Introduce cc del cliente: ')
        if cc in empleados:
            del empleados[cc]
        else:
            print('No existe el cliente con el cc', cc)
    if opcion =='4':
        cc = input('Introduce c.c del cliente: ')
        nombre = input('Introduce el nombre correcto del empleado: ')
        cliente = {'nombre':nombre}
        empleados[cc] = cliente
    opcion = input('Menú\n(1) Añadir empleados\n(2) Imprimir\n(3) Eliminar\n(4) Editar \n(5) Salir\nElige una opción:')
    

