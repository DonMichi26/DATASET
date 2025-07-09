# Proyecto de Detección de Iglesias y Más con YOLOv8

Este proyecto utiliza un modelo YOLOv8 entrenado para detectar iglesias, campanas, puertas y otros objetos en imágenes. Incluye una interfaz web sencilla basada en Gradio para subir imágenes y visualizar los resultados de detección.

---

## Requisitos

- Python 3.8 o superior
- pip

---

## Instalación de dependencias

```bash
pip install ultralytics gradio
```

---

## Estructura del proyecto

```
├── app.py                        # Interfaz web Gradio
├── entrenar.py                   # Script de entrenamiento (opcional)
├── data.yaml                     # Configuración de dataset y clases
├── train/                        # Imágenes y anotaciones de entrenamiento
├── valid/                        # Imágenes y anotaciones de validación
├── test/                         # Imágenes y anotaciones de prueba
├── runs/
│   └── detect/
│       └── iglesias_modelo22/
│           └── weights/
│               ├── best.pt       # Pesos del modelo entrenado (usar este)
│               └── last.pt       # Último checkpoint (opcional)
```

---

## Cómo ejecutar la interfaz web

1. Asegúrate de tener el archivo de pesos en `runs/detect/iglesias_modelo22/weights/best.pt`.
2. Ejecuta el siguiente comando:

```bash
python app.py
```

3. Abre tu navegador y accede a:

```
http://localhost:7860
```

4. Sube una imagen y visualiza los resultados de detección.

---

## Cómo hacer inferencias desde la terminal

```bash
yolo detect predict model="runs/detect/iglesias_modelo22/weights/best.pt" source="ruta/a/tu/imagen.jpg"
```

---

## Entrenamiento (opcional)

Si quieres reentrenar el modelo, edita y ejecuta `entrenar.py`.

---

## Despliegue en servidor

- Para exponer la app en una red local, accede desde otra PC usando la IP del servidor: `http://IP_DEL_SERVIDOR:7860`
- Para producción, se recomienda usar un proxy inverso (Nginx, Apache) y/o servicios como Render, Railway, Hugging Face Spaces, etc.

---

## Notas

- El modelo solo detecta las clases con las que fue entrenado (ver `data.yaml`).
- Puedes limpiar resultados viejos borrando el contenido de `runs/detect/predict/`.
- Si tienes dudas, revisa los scripts y la estructura del proyecto. 