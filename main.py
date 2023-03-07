import argparse
import PIL.Image
import PIL.ImageEnhance
import PIL.ImageFilter
import PIL.ImageOps


def crop_image(im, left, upper, right, lower):
    return im.crop((left, upper, right, lower))


def resize_image(im, width, height):
    return im.resize((width, height))


def flip_image(im):
    return im.transpose(PIL.Image.FLIP_LEFT_RIGHT)


def rotate_image(im, degrees):
    return im.rotate(degrees)


def compress_image(im, quality):
    im.save("Image1.jpg", optimize=True, quality=quality)


def blur_image(im):
    return im.filter(PIL.ImageFilter.BLUR)


def sharpen_image(im):
    return im.filter(PIL.ImageFilter.SHARPEN)


def set_brightness(im, factor):
    enhancer = PIL.ImageEnhance.Brightness(im)
    return enhancer.enhance(factor)


def set_contrast(im, factor):
    enhancer = PIL.ImageEnhance.Contrast(im)
    return enhancer.enhance(factor)


def add_filters(im):
    im = PIL.ImageOps.grayscale(im)
    im = PIL.ImageOps.invert(im)
    im = PIL.ImageOps.posterize(im, 4)
    return im


def main():
    # Crear el objeto parser y definir los argumentos
    parser = argparse.ArgumentParser(description='Script para optimizar imágenes.')
    parser.add_argument('imagen', type=str, help='Nombre de la imagen a procesar')
    parser.add_argument('--crop', nargs=4, type=int, metavar=('left', 'upper', 'right', 'lower'),
                        help='Recortar la imagen en las coordenadas indicadas')
    parser.add_argument('--resize', nargs=2, type=int, metavar=('width', 'height'),
                        help='Cambiar el tamaño de la imagen a los valores indicados')
    parser.add_argument('--flip', action='store_true', help='Voltear la imagen horizontalmente')
    parser.add_argument('--rotate', type=int, metavar='degrees', help='Rotar la imagen el número de grados indicado')
    parser.add_argument('--compress', type=int, metavar='quality', help='Comprimir la imagen con la calidad indicada')
    parser.add_argument('--blur', action='store_true', help='Aplicar efecto de desenfoque')
    parser.add_argument('--sharpen', action='store_true', help='Aplicar efecto de enfoque')
    parser.add_argument('--brightness', type=float, metavar='factor', help='Ajustar el brillo de la imagen')
    parser.add_argument('--contrast', type=float, metavar='factor', help='Ajustar el contraste de la imagen')
    parser.add_argument('--filters', action='store_true', help='Aplicar filtros a la imagen')
    args = parser.parse_args()

    # Abrir la imagen
    im = PIL.Image.open(args.imagen)

    # Aplicar las transformaciones según los argumentos indicados
    if args.crop:
        im = crop_image(im, *args.crop)
    if args.resize:
        im = resize_image(im, *args.resize)
    if args.flip:
        im = flip_image(im)
    if args.rotate:
        im = rotate_image(im, args.rotate)
    if args.compress:
        compress_image(im, args.compress)
    if args.blur:
        im = blur_image(im)
    if args.sharpen:
        im = sharpen_image(im)
    if args.brightness:
        im = set_brightness(im, args.brightness)
    if args.contrast:
		im = set_contrast(im, args.contrast)
	if args.filters:
		im = add_filters(im)

	# Guardar la imagen
	im.save(args.imagen)

if __name__ == '__main__':
	main()
