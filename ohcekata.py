import datetime

class OhceKata:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        hora = datetime.datetime.now().hour
        if (20 <= hora < 6):
            return f"¡Buenas noches {self.nombre}!"
        elif (6 <= hora < 12):
            return f"¡Buenos dias {self.nombre}!"
        else:
            return f"¡Buenas tardes {self.nombre}!"