
class Node:
    def __init__(self, datos):
        self.datos = datos
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar_final(self, datos):
        new_node = Node(datos)
        if(self.head is None):
            self.head = new_node
            return
        current = self.head
        while(current.next):
           current = current.next

        current.next = new_node