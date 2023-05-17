from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.fila = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.fila)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.fila.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if (self.__len__()):
            return self.fila.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if (index >= 0 and index <= len(self.fila) - 1):
            return self.fila[index]
        else:
            raise IndexError('Índice Inválido ou Inexistente')
