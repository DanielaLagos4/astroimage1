import cv2
import numpy as np

def detect_objects(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral adaptativo para segmentar los objetos
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Realizar una operación de apertura para eliminar el ruido y suavizar los bordes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

    # Encontrar los contornos de los objetos detectados
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    objects_image = np.copy(image)
    cv2.drawContours(objects_image, contours, -1, (0, 255, 0), 2)

    return objects_image

# Cargar la imagen astronómica
image = cv2.imread("C:/Users/lagos/Downloads/space-331.jpg")

# Detectar objetos astronómicos en la imagen
detected_objects = detect_objects(image)

# Mostrar la imagen original y la imagen con los objetos detectados
cv2.imshow("Imagen Original", image)
cv2.imshow("Objetos Detectados", detected_objects)
cv2.waitKey(0)
cv2.destroyAllWindows()


