import pyautogui
import time

def mover_raton(intervalo=30):
    """Mueve el ratón ligeramente cada `intervalo` segundos para evitar inactividad en Colab."""
    screenWidth, screenHeight = pyautogui.size()  # Obtener el tamaño de la pantalla

    while True:
        x, y = pyautogui.position()  # Obtener la posición actual del cursor

        # Verificar si el ratón está en una esquina y corregirlo
        if (x == 0 and y == 0) or (x == 0 and y == screenHeight) or (x == screenWidth and y == 0) or (x == screenWidth and y == screenHeight):
            print("El ratón está en una esquina, moviéndolo al centro para evitar error.")
            pyautogui.moveTo(screenWidth // 2, screenHeight // 2)  # Moverlo al centro de la pantalla
            time.sleep(0.5)  # Pequeña pausa

        # Mover el ratón ligeramente
        pyautogui.moveTo(x + 1, y + 1)
        time.sleep(0.5)  # Pequeña pausa
        pyautogui.moveTo(x, y)  # Regresarlo a la posición original
        time.sleep(intervalo)  # Esperar antes del siguiente movimiento

        print("Ratón movido")

# Ejecutar la función en un bucle infinito
mover_raton()

