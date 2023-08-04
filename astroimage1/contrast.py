import cv2

def adjust_contrast(image, alpha, beta):
    # Ajustar el contraste utilizando la transformación lineal
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return adjusted_image

# Cargar la imagen astronómica
image = cv2.imread("C:/Users/lagos/Downloads/PHOTO-2023-04-20-22-56-58.jpg")

# Ajustar el contraste de la imagen
adjusted_image = adjust_contrast(image, alpha=1.5, beta=0)

# Mostrar la imagen original y la imagen con el contraste ajustado
cv2.imshow("Imagen Original", image)
cv2.imshow("Imagen con Contraste Ajustado", adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#En este código, la función adjust_contrast toma una imagen, un factor de contraste alpha y un factor de brillo beta como parámetros. Utiliza la función cv2.convertScaleAbs para ajustar el contraste de la imagen utilizando una transformación lineal.
#Después de definir la función adjust_contrast, cargamos la imagen astronómica (image) y aplicamos el ajuste de contraste llamando a la función adjust_contrast. Finalmente, mostramos la imagen original y la imagen con el contraste ajustado utilizando imshow de OpenCV.
#Asegúrate de reemplazar "ruta/a/la/imagen.jpg" con la ruta y el nombre de archivo de tu propia imagen astronómica.
#Puedes ajustar los valores de alpha y beta según tus necesidades para obtener el nivel de contraste deseado en la imagen ajustada. El valor de alpha controla el contraste y el valor de beta controla el brillo.