import cv2

# Cargar una imagen
image = cv2.imread("C:/Users/lagos/Downloads/PHOTO-2023-04-20-22-56-58.jpg")

# Mostrar la imagen original
cv2.imshow("Imagen original", image)
cv2.waitKey(0)

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow("Imagen en escala de grises", gray_image)
cv2.waitKey(0)

# Aplicar un filtro de desenfoque a la imagen
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Mostrar la imagen desenfocada
cv2.imshow("Imagen desenfocada", blurred_image)
cv2.waitKey(0)

# Detectar bordes en la imagen utilizando el operador de Canny
edges = cv2.Canny(gray_image, 100, 200)

# Mostrar los bordes detectados
cv2.imshow("Bordes detectados", edges)
cv2.waitKey(0)

# Guardar la imagen procesada
cv2.imwrite("procesadas.jpg", image)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()