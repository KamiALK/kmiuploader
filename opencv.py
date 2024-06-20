import cv2
import pytesseract
from moviepy.editor import VideoFileClip
import numpy as np

# Ruta al archivo de video
video_path = "/home/kamilo/Descargas/prueba.mp4"


# Función para modificar el color del texto a blanco (255, 255, 255) y el resto a negro (0, 0, 0)
def modify_text_color(frame):
    # Convertir el fotograma a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para binarizar el fotograma
    _, binary_frame = cv2.threshold(gray_frame, 150, 255, cv2.THRESH_BINARY)

    # Convertir el fotograma binarizado a color (blanco)
    white_text_frame = cv2.cvtColor(binary_frame, cv2.COLOR_GRAY2BGR)
    white_text_frame[np.where((white_text_frame != [255, 255, 255]).all(axis=2))] = [
        0,
        0,
        0,
    ]

    return white_text_frame


# Función para extraer texto de un fotograma
def extract_text_from_frame(frame):
    # Usar pytesseract para obtener texto del fotograma
    text = pytesseract.image_to_string(frame)

    return text


# Función para verificar si el contorno es lo suficientemente pequeño para ser considerado texto
def is_small_contour(contour, min_area_threshold):
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    return area < min_area_threshold


# Parámetros
min_area_threshold = (
    20000  # Umbral de área mínimo para considerar el contorno como texto
)

# Abrir el video
video = VideoFileClip(video_path)

# Iterar sobre cada fotograma del video
for idx, frame in enumerate(video.iter_frames(fps=video.fps)):
    # Modificar el color del texto a blanco (255, 255, 255) y el resto a negro (0, 0, 0)
    white_text_frame = modify_text_color(frame)

    # Encontrar contornos en el fotograma binarizado
    gray_frame = cv2.cvtColor(white_text_frame, cv2.COLOR_BGR2GRAY)
    _, binary_frame = cv2.threshold(gray_frame, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        binary_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Filtrar contornos basados en el área
    filtered_contours = [
        cnt for cnt in contours if is_small_contour(cnt, min_area_threshold)
    ]

    # Dibujar contornos pequeños (para propósitos de visualización)
    cv2.drawContours(white_text_frame, filtered_contours, -1, (0, 255, 0), 2)

    # Extraer texto del fotograma modificado (solo de regiones pequeñas)
    text = extract_text_from_frame(white_text_frame)

    # Imprimir el texto extraído
    print(f"Texto en el fotograma {idx}:")
    print(text)
    print("=" * 20)

# Cerrar el video después de usarlo
video.close()
