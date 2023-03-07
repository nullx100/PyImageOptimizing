ImageOptimizing

Este es un script en Python para optimizar imágenes de forma sencilla y automatizada mediante la línea de comandos. El script utiliza la biblioteca Pillow para aplicar diferentes transformaciones a las imágenes, como recorte, cambio de tamaño, volteo, rotación, ajuste de brillo y contraste, aplicación de filtros, entre otros. El uso de argumentos en la línea de comandos hace que el proceso de optimización sea fácil y rápido para el usuario.
Requerimientos

El script requiere Python 3 y la biblioteca Pillow, que se puede instalar con el siguiente comando:

pip install Pillow

Uso

El script se ejecuta desde la línea de comandos con la siguiente sintaxis:

css

python image_optimizing.py imagen.jpg [opciones]

Donde imagen.jpg es el nombre del archivo de imagen a procesar, y [opciones] son las diferentes transformaciones que se quieren aplicar sobre la imagen.

A continuación se detallan las opciones disponibles:
Recorte

Para recortar la imagen en las coordenadas indicadas, se utiliza la opción --crop seguida de las coordenadas de las cuatro esquinas en el siguiente orden: left, upper, right, lower. Por ejemplo:

css

python image_optimizing.py imagen.jpg --crop 34 23 100 100

Este comando recortaría la imagen en las coordenadas (34, 23) y (100, 100).
Cambio de tamaño

Para cambiar el tamaño de la imagen a los valores indicados, se utiliza la opción --resize seguida del ancho y el alto deseado. Por ejemplo:

css

python image_optimizing.py imagen.jpg --resize 500 500

Este comando cambiaría el tamaño de la imagen a 500x500 píxeles.
Volteo

Para voltear la imagen horizontalmente, se utiliza la opción --flip. Por ejemplo:

css

python image_optimizing.py imagen.jpg --flip

Este comando voltearía la imagen horizontalmente.
Rotación

Para rotar la imagen un número de grados, se utiliza la opción --rotate seguida del número de grados a rotar. Por ejemplo:

css

python image_optimizing.py imagen.jpg --rotate 90

Este comando rotaría la imagen 90 grados en sentido horario.
Compresión

Para comprimir la imagen con una calidad indicada, se utiliza la opción --compress seguida de la calidad deseada en una escala de 0 a 100. Por ejemplo:

css

python image_optimizing.py imagen.jpg --compress 80

Este comando comprimiría la imagen con una calidad del 80%.
Desenfoque

Para aplicar un efecto de desenfoque a la imagen, se utiliza la opción --blur. Por ejemplo:

css

python image_optimizing.py imagen.jpg --blur

Este comando aplicaría un efecto de desenfoque a la imagen.
Enfoque

Para aplicar un efecto de enfoque a la imagen, se utiliza la opción --sharpen. Por ejemplo:

css

python image_optimizing.py imagen.jpg --sharpen

Este comando aplicaría un efecto de enfoque a la imagen.

Brillo

Para ajustar el brillo de la imagen, se utiliza la opción --brightness seguida del factor de brillo deseado en una escala de 0 a infinito. El valor 1 no modifica el brillo, valores menores lo reducen y valores mayores lo aumentan. Por ejemplo:

css

python image_optimizing.py imagen.jpg --brightness 1.5

Este comando aumentaría el brillo de la imagen en un 50%.
Contraste

Para ajustar el contraste de la imagen, se utiliza la opción --contrast seguida del factor de contraste deseado en una escala de 0 a infinito. El valor 1 no modifica el contraste, valores menores lo reducen y valores mayores lo aumentan. Por ejemplo:

css

python image_optimizing.py imagen.jpg --contrast 1.5

Este comando aumentaría el contraste de la imagen en un 50%.
Filtros

Para aplicar filtros a la imagen, se utiliza la opción --filters. Los filtros que se aplican son la conversión a escala de grises, la inversión de colores y la reducción del número de niveles de color (posterización). Por ejemplo:

css

python image_optimizing.py imagen.jpg --filters

Este comando aplicaría los filtros mencionados a la imagen.
Contribuir

Este es un proyecto de código abierto y se aceptan contribuciones. Si quieres contribuir al proyecto, por favor lee el archivo CONTRIBUTING.md para conocer las pautas de contribución.
Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo LICENSE.md para más información.
