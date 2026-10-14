class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        # self.anterior = None  # Equivalente al //Nodo* anterior;

# Función para agregar elementos a la lista
def agregar_nodo(cabeza, valor):
    nuevo_nodo = Nodo(dato=valor) # Creando el apuntador hacia el nuevo nodo

    if cabeza is None:
        cabeza = nuevo_nodo
    else:
        actual = cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo
        
    return cabeza # Retornamos la cabeza actualizada

# Función para imprimir la lista
def imprimir_lista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.dato, end=" ")
        actual = actual.siguiente
    
    print()

# Función para borrar la lista
def borrar_lista(cabeza):
    while cabeza is not None:
        siguiente = cabeza.siguiente
        
        del cabeza # Borrado simbólico (Python usa recolector de basura)
        cabeza = siguiente
        
        print("Elemento borrado ")

def main():
    cabeza = None # Declaramos un puntero de memoria nulo

    tamano_lista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))

    if tamano_lista <= 0:
        print("Cantidad de elementos no valida")
        return 1

    for i in range(tamano_lista):
        valor = int(input(f"Ingrese dato {i + 1}: "))
        # Invocamos nuestra función de agregar Nodo
        cabeza = agregar_nodo(cabeza, valor)

    print("Imprimiendo Lista de numeros")
    imprimir_lista(cabeza)

    borrar_lista(cabeza)

    return 0

# Punto de entrada del programa
if __name__ == "__main__":
    main()
