from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Lista de pasajeros con los métodos de list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            print('  Ya existe ese número de pasajero')
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print('  (lista vacía)')
            return
        for i, p in enumerate(self.pasajeros):
            print(f'  [{i}] {p}')

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            return False
        if self.buscar(pasajero.numero) != -1:
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        if posiciones:
            return posiciones[0]
        return -1

    def esta_ordenada_asc(self):
        return all(self.pasajeros[i].numero <= self.pasajeros[i + 1].numero
                   for i in range(len(self.pasajeros) - 1))

    def buscar_binaria(self, numero):
        if not self.esta_ordenada_asc():
            return -1
        numeros = [p.numero for p in self.pasajeros]
        posicion = bisect_left(numeros, numero)
        if posicion < len(numeros) and numeros[posicion] == numero:
            return posicion
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        if self.buscar(numero) == -1:
            return False
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = [Pasajero(p.numero, p.nombre, p.cedula, p.edad,
                                   p.fecha_vuelo, p.destino, p.asiento)
                           for p in self.pasajeros]
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]
