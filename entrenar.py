from ultralytics import YOLO

# Ruta al archivo data.yaml (ajusta si lo mueves)
data_yaml = "C:/Users/jeanc/OneDrive/Documentos/iglesias_dataset/data.yaml"

# Cargar modelo base YOLOv8 nano (rápido y ligero)
model = YOLO("yolov8n.pt")  # puedes cambiar por "yolov8s.pt" para más precisión

# Entrenamiento
model.train(
    data=data_yaml,
    epochs=100,
    device='cpu',  # Fuerza el uso de CPU
    name="iglesias_modelo2"
)
