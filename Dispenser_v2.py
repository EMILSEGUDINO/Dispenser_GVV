from datetime import datetime, time
import time as tm

class Dispositivo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False  # False = Apagado, True = Encendido

    def encender(self):
        self.estado = True
        print(f'{self.nombre} encendido.')

    def apagar(self):
        self.estado = False
        print(f'{self.nombre} apagado.')

    def leer_estado(self):
        return 'Encendido' if self.estado else 'Apagado'


class Dispenser(Dispositivo):
  
    def __init__(self, nombre):
        super().__init__(nombre)

    def dispensar(self):
        if self.estado:
            print(f'{self.nombre} está dispensando...')
        else:
            print(f'{self.nombre} está apagado.')


class ControladorHorario:
    
    def __init__(self, dispositivo, hora_inicio, hora_fin):
        self.dispositivo = dispositivo
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def controlar(self):
        hora_actual = datetime.now().time()
        print(f'Hora actual: {hora_actual}')  # Imprimir la hora actual
        print(f'Hora inicio: {self.hora_inicio}, Hora fin: {self.hora_fin}')  # Imprimir el rango horario

        if self.hora_inicio <= hora_actual <= self.hora_fin:
            if not self.dispositivo.estado:
                print('Dentro del horario, encendiendo dispositivo...')
                self.dispositivo.encender()
        else:
            if self.dispositivo.estado:
                print('Fuera del horario, apagando dispositivo...')
                self.dispositivo.apagar()


# Crear una instancia del Dispenser
dispensador = Dispenser('Dispenser de Agua')

# Franja horaria de encendido: 6:00 AM a 6:00 PM
controlador = ControladorHorario(dispensador, time(6, 0), time(18, 0))

for _ in range(3):
    controlador.controlar()
    print(f'Estado del {dispensador.nombre}: {dispensador.leer_estado()}')
    tm.sleep(2)