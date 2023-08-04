import cv2

def remove_noise(image, method='median', kernel_size=3):
    if method == 'median':
        # Aplicar filtro de mediana para eliminar el ruido
        filtered_image = cv2.medianBlur(image, kernel_size)
    elif method == 'gaussian':
        # Aplicar filtro gaussiano para suavizar la imagen
        filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    else:
        raise ValueError('Método de reducción de ruido no válido')

    return filtered_image

# Cargar la imagen astronómica con ruido
image_with_noise = cv2.imread("C:/Users/lagos/Downloads/PHOTO-2023-04-20-22-56-58.jpg")

# Aplicar el método de reducción de ruido
filtered_image = remove_noise(image_with_noise, method='median', kernel_size=3)

# Mostrar la imagen original y la imagen filtrada
cv2.imshow("Imagen Original", image_with_noise)
cv2.imshow("Imagen Filtrada", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
