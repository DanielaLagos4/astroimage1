import numpy as np
import glob

def stack_images(image_paths, method='mean'):
    # Leer las imágenes alineadas desde las rutas de archivo proporcionadas
    aligned_images = [cv2.imread(path) for path in image_paths]

    # Verificar si hay imágenes alineadas
    if len(aligned_images) == 0:
        raise ValueError('No se proporcionaron imágenes alineadas')

    # Verificar si todas las imágenes tienen el mismo tamaño
    image_shape = aligned_images[0].shape
    if not all(image.shape == image_shape for image in aligned_images):
        raise ValueError('Las imágenes alineadas no tienen el mismo tamaño')

    # Convertir las imágenes a tipo float32 para evitar desbordamiento
    aligned_images = [image.astype(np.float32) for image in aligned_images]

    # Apilar las imágenes utilizando el método seleccionado
    if method == 'mean':
        stacked_image = np.mean(aligned_images, axis=0)
    elif method == 'sum':
        stacked_image = np.sum(aligned_images, axis=0)
    else:
        raise ValueError('Método de apilamiento no válido')

    # Convertir la imagen apilada nuevamente a tipo uint8
    stacked_image = stacked_image.astype(np.uint8)

    return stacked_image

# Obtener las rutas de archivo de las imágenes alineadas
image_paths = glob.glob("ruta/a/imagenes_alineadas/*.jpg")

# Realizar el apilamiento de imágenes utilizando el método promedio
stacked_image = stack_images(image_paths, method='mean')

# Mostrar la imagen apilada
cv2.imshow("Imagen Apilada", stacked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()