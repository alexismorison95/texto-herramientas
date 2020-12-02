# Quitar justificados, guiones y saltos de línea

Herramienta de consola para quitar el formato molesto del texto de algunos PDFs. La idea surgió debido a la necesidad de sacar información de distintos PDFs a la hora de hacer trabajos prácticos, y que estos estén en un formato molesto y que acomodarlo en un archivo Word lleve mucho tiempo.

## Uso

Ejecutar el script:
```bash
$ python main.py
```

## Parámetros

* Input y Output

    ```bash
    $ python main.py -i {entrada.txt} -o {salida.txt}
    ```

* Quitar justificado

    ```bash
    $ python main.py -i {entrada.txt} -o {salida.txt} -j
    ```

* Quitar guiones y saltos de línea

    ```bash
    $ python main.py -i {entrada.txt} -o {salida.txt} -g
    ```

## Ejemplo

Mirar los archivos:

    > text.txt
    > output.txt