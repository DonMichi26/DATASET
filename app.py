import gradio as gr
from ultralytics import YOLO

# Carga tu modelo entrenado
model = YOLO("runs/detect/iglesias_modelo22/weights/best.pt")

def detectar(imagen):
    # Realiza la predicción
    resultados = model.predict(source=imagen, save=False)
    # Obtiene la imagen con las detecciones
    imagen_resultado = resultados[0].plot()  # Devuelve una imagen numpy
    return imagen_resultado

# Crea la interfaz
app = gr.Interface(
    fn=detectar,
    inputs=gr.Image(type="filepath", label="Sube una imagen"),
    outputs=gr.Image(type="numpy", label="Resultado"),
    title="Detección de Iglesias",
    description="Sube una imagen y el modelo detectará las iglesias."
)

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860) 