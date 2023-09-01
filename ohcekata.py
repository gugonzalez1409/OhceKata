import datetime

class OhceKata:
    def saludo(self):
        hora = datetime.datetime.now().hour
        if (20 <= hora < 6):
            return("Buenas noches")
        elif (6 <= hora < 12):
            return ("Buenos dias")
        else:
            return("Buenas tardes")