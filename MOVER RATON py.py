
# Mover el ratón ligeramente cada cierto tiempo para evitar inactividad en Colab
import pyautogui
import time

def mover_raton(intervalo=30):
    """Mueve el ratón ligeramente cada `intervalo` segundos para evitar inactividad en Colab."""
    while True:
        x, y = pyautogui.position()  # Obtener la posición actual del cursor
        pyautogui.moveTo(x + 1, y + 1)  # Moverlo ligeramente
        time.sleep(0.5)  # Pequeña pausa
        pyautogui.moveTo(x, y)  # Regresarlo a la posición original
        time.sleep(intervalo)  # Esperar antes del siguiente movimiento
        print("Ratón movido")

# Ejecutar la función en un bucle infinito
mover_raton()
