# Quitar justificados, guiones y saltos de línea

Herramienta de consola para quitar el formato molesto del texto de algunos PDFs. La idea surgió debido a la necesidad de sacar información de distintos PDFs a la hora de hacer trabajos prácticos, y que estos estén en un formato molesto y que acomodarlo en un archivo Word lleve mucho tiempo.

# Uso

Ver ayuda:
```bash
$ python main.py -h
```

## Parámetros

* Input

    **Hay 2 formas de ingresar el texto:**

    - Por consola

        ```bash
        $ python main.py -i "Mi texto"
        ```
    - Por archivo
        ```bash
        $ python main.py -i texto.txt
        ```

* Output

    **Si no se proporciona este argumento se mostrará el resultado en la consola.**

    ```bash
    $ python main.py -o resultado.txt
    ```

* Quitar justificado

    ```bash
    $ python main.py -j
    ```

* Quitar guiones y saltos de línea

    ```bash
    $ python main.py -g
    ```

## Ejemplo

```bash
$ python main.py -i text.txt -o output.txt -g
```

Mirar los archivos:

    > text.txt
    > output.txt