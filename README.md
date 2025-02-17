# Mover Ratón Automáticamente en Python

Este script en Python mueve el cursor del ratón de forma automática para evitar la detección de inactividad en plataformas como Google Colab, evitando que la sesión se cierre.

## Requisitos

Asegúrate de tener instalado Python y la librería `pyautogui`. Si no la tienes instalada, ejecúta:

```bash
pip install pyautogui
```

Para usuarios de **Anaconda**, usa:

```bash
conda install -c conda-forge pyautogui
```

## Uso

Guarda el siguiente código en un archivo Python (`mover_raton.py`) y ejecútalo:

```python
import pyautogui
import time

def mover_raton(intervalo=30):
    """Mueve el cursor ligeramente cada `intervalo` segundos."""
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 1, y + 1)
        time.sleep(0.5)
        pyautogui.moveTo(x, y)
        time.sleep(intervalo)

# Iniciar el movimiento del ratón
mover_raton()
```

## Explicación
- El script mueve el cursor **1 píxel a la derecha y abajo**, luego lo regresa a su posición original.
- Se ejecuta cada **30 segundos** (puedes cambiarlo en `intervalo`).
- Previene que plataformas como **Google Colab** detecten inactividad y cierren la sesión.

## Detener el Script
Para detener el script, presiona **Ctrl + C** en la terminal o cierra la ventana de ejecución.

## Solución de Problemas
Si obtienes el error:

```plaintext
Import "pyautogui" could not be resolved from source
```

1. **Verifica que `pyautogui` está instalado**:
   ```bash
   python -m pip show pyautogui
   ```
   Si no aparece, vuelve a instalarlo.

2. **Asegúrate de ejecutar Python con el mismo entorno donde instalaste `pyautogui`**:
   ```bash
   python -m pip install pyautogui
   ```

3. **Si usas `VS Code` y Pylance**, puede ser un problema del analizador de código. Reinicia el editor o prueba ejecutar el script desde una terminal.

---

**¡Listo! Ahora tu sesión no se cerrará por inactividad! 🚀**

