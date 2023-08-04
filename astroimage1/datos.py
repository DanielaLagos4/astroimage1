import cv2
import numpy as np

def measure_properties(contours):
    properties = []

    for contour in contours:
        # Calcular el centroide del contorno
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # Calcular el área del contorno
        area = cv2.contourArea(contour)

        # Calcular el perímetro del contorno
        perimeter = cv2.arcLength(contour, True)

        # Agregar las propiedades del objeto a la lista
        properties.append({'centroid': (cx, cy), 'area': area, 'perimeter': perimeter})

    return properties

# Cargar la imagen astronómica
image = cv2.imread("C:/Users/lagos/Downloads/PHOTO-2023-04-20-22-56-58.jpg")

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral adaptativo para segmentar los objetos
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Realizar una operación de apertura para eliminar el ruido y suavizar los bordes
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

# Encontrar los contornos de los objetos detectados
contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Medir las propiedades de los objetos detectados
object_properties = measure_properties(contours)

# Mostrar las propiedades de los objetos detectados
for i, prop in enumerate(object_properties):
    centroid = prop['centroid']
    area = prop['area']
    perimeter = prop['perimeter']
    print(f"Objeto {i+1}: Centroid: {centroid}, Area: {area}, Perimeter: {perimeter}")


