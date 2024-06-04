import time

# Variables
dispenser_state = "off"

# franja horaria de encendido (en formato HH:MM)
start_time = "06:00"
end_time = "18:00"

def is_in_time_range():
    
    current_time = datetime.datetime.now()
    start_time_obj = datetime.datetime.strptime(start_time, "%H:%M")
    end_time_obj = datetime.datetime.strptime(end_time, "%H:%M")

    if start_time_obj <= current_time <= end_time_obj:
        return True
    else:
        return False

while True:
 
    if is_in_time_range():
        if dispenser_state == "off":
            print("Dispensador de agua encendido")
            dispenser_state = "on"
    else:
        if dispenser_state == "on":
            print("Dispensador de agua apagado")
            dispenser_state = "off"

    # Esperar 1 minuto
    time.sleep(60)
