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

    def invertir_palabra(self, input):
        return input[::-1]
    
    def palindromo(self, input):
        input_invertido = input[::-1]
        if(input == input_invertido):
            return f"{input_invertido}\n¡Bonita palabra!"
        return input_invertido