from datetime import datetime
from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            numero = int(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f'  Escribe un número mayor o igual a {minimo}.')
            else:
                return numero
        except ValueError:
            print('  Debe ser un número entero.')


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print('  Este campo no puede estar vacío.')


def leer_fecha():
    while True:
        fecha = leer_texto('  Fecha de vuelo (AAAA-MM-DD): ')
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            return fecha
        except ValueError:
            print('  Fecha no válida. Utiliza AAAA-MM-DD.')


def leer_pasajero():
    numero = leer_entero('  N.º de pasajero: ', 1)
    nombre = leer_texto('  Nombre: ')
    cedula = leer_texto('  Cédula: ')
    edad = leer_entero('  Edad: ', 0)
    fecha = leer_fecha()
    destino = leer_texto('  Destino: ')
    asiento = leer_texto('  Asiento: ').upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = (
        (1005, 'Diana', '0923456789', 22, '2026-11-15', 'Quito', '12A'),
        (1002, 'Ana', '0912345678', 28, '2026-11-15', 'Lima', '03C'),
        (1009, 'Luis', '0987654321', 35, '2026-11-20', 'Bogotá', '18F'),
        (1004, 'Beto', '0934567890', 16, '2026-11-20', 'Quito', '07B'),
        (1001, 'Elena', '0901234567', 41, '2026-11-22', 'Lima', '01A'),
    )
    agregados = 0
    for datos_pasajero in datos:
        if lista.buscar(datos_pasajero[0]) == -1:
            if lista.añadir(Pasajero(*datos_pasajero)):
                agregados += 1
    print(f'  Datos de prueba: {agregados} pasajeros agregados.')


def mostrar_opciones(titulo, extras=False):
    print(f'\n========== {titulo} ==========')
    print(' 1. Añadir           2. Listar            3. Insertar en posición')
    print(' 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar')
    print(' 7. Eliminar por posición                 8. Eliminar por número')
    print(' 9. Ordenar asc     10. Ordenar desc     11. Reversar')
    print('12. Copiar          13. Longitud')
    if extras:
        print('14. Filtrar por destino                  15. Mayores de edad')
    print(' C. Cargar datos de prueba                0. Volver')


def mostrar_resultados(pasajeros):
    if not pasajeros:
        print('  No hay pasajeros que coincidan.')
    else:
        for pasajero in pasajeros:
            print(' ', pasajero)


def ejecutar_menu(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        op = input('Opción: ').strip().upper()

        if op == '1':
            pasajero = leer_pasajero()
            if lista.añadir(pasajero):
                print('  Pasajero añadido.')
            else:
                print('  No fue posible añadir el pasajero.')

        elif op == '2':
            lista.listar()

        elif op == '3':
            posicion = leer_entero('  Posición para insertar: ')
            if posicion < 0 or posicion > lista.longitud():
                print('  Posición inválida.')
            else:
                pasajero = leer_pasajero()
                if lista.insertar(posicion, pasajero):
                    print('  Pasajero insertado.')
                else:
                    print('  No se pudo insertar: lista llena o número repetido.')

        elif op == '4':
            numero = leer_entero('  Número a buscar: ')
            posicion = lista.buscar(numero)
            if posicion == -1:
                print('  El pasajero no existe.')
            else:
                print(f'  Encontrado en [{posicion}].')
                if isinstance(lista, MiLista):
                    print(' ', lista.datos[posicion])
                else:
                    print(' ', lista.pasajeros[posicion])

        elif op == '5':
            if not lista.esta_ordenada_asc():
                print('  Primero debes ordenar ascendentemente (opción 9).')
            else:
                numero = leer_entero('  Número a buscar: ')
                posicion = lista.buscar_binaria(numero)
                if posicion == -1:
                    print('  El pasajero no existe.')
                else:
                    print(f'  Encontrado en [{posicion}].')
                    if isinstance(lista, MiLista):
                        print(' ', lista.datos[posicion])
                    else:
                        print(' ', lista.pasajeros[posicion])

        elif op == '6':
            numero = leer_entero('  Número del pasajero: ')
            destino = leer_texto('  Nuevo destino: ')
            asiento = leer_texto('  Nuevo asiento: ').upper()
            if lista.modificar(numero, destino, asiento):
                print('  Pasajero modificado.')
            else:
                print('  Pasajero no encontrado.')

        elif op == '7':
            posicion = leer_entero('  Posición a eliminar: ')
            eliminado = lista.eliminar_por_posicion(posicion)
            if eliminado is None:
                print('  Posición inválida.')
            else:
                print('  Eliminado:', eliminado)

        elif op == '8':
            numero = leer_entero('  Número a eliminar: ')
            if lista.eliminar_por_valor(numero):
                print('  Pasajero eliminado.')
            else:
                print('  Pasajero no encontrado.')

        elif op == '9':
            lista.ordenar_asc()
            print('  Lista ordenada de menor a mayor.')
            lista.listar()

        elif op == '10':
            lista.ordenar_desc()
            print('  Lista ordenada de mayor a menor.')
            lista.listar()

        elif op == '11':
            lista.reversar()
            print('  Orden invertido.')
            lista.listar()

        elif op == '12':
            copia = lista.copiar()
            print('  Copia creada. Contenido de la copia:')
            copia.listar()
            print('  Se invierte únicamente la copia para comprobar independencia:')
            copia.reversar()
            copia.listar()
            print('  Lista original (sin cambios):')
            lista.listar()

        elif op == '13':
            print(f'  Total de pasajeros: {lista.longitud()}')

        elif op == '14' and extras:
            destino = leer_texto('  Destino que deseas filtrar: ')
            mostrar_resultados(lista.filtrar_por_destino(destino))

        elif op == '15' and extras:
            mostrar_resultados(lista.mayores_de_edad())

        elif op == 'C':
            cargar_datos_prueba(lista)

        elif op == '0':
            break

        else:
            print('  Opción no válida.')


def menu_lista1():
    ejecutar_menu(lista1, 'MENÚ 1 · MiLista')


def menu_lista2():
    ejecutar_menu(lista2, 'MENÚ 2 · list de Python', extras=True)


def main():
    while True:
        print('\n===== TAREA LISTAS · PASAJEROS =====')
        print('1. Menú 1 · MiLista')
        print('2. Menú 2 · list de Python')
        print('3. Salir')
        op = input('Opción: ').strip()
        if op == '1':
            menu_lista1()
        elif op == '2':
            menu_lista2()
        elif op == '3':
            print('¡Hasta pronto!')
            break
        else:
            print('Opción no válida.')


if __name__ == '__main__':
    main()
