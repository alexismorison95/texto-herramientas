from argparse import ArgumentParser
from argparse import FileType

from sys import stdin
from sys import stdout



def parseArgs():

    parser = ArgumentParser(description=__doc__)

    parser.add_argument('-i',
                        '--input',
                        help='Leer el texto desde un archivo o desde la consola entre comillas dobles. Ej: -i "mi texto", o -i texto.txt',
                        default=stdin)
    
    parser.add_argument('-o',
                        '--output',
                        help='Escribir resultado en un archivo, si no se usa el argumento se mostrará el resultado en la consola. Ej: -o resultado.txt',
                        default=False)

    parser.add_argument('-j',
                        '--justificado',
                        action="store_true",
                        help='Quitar justificado',
                        default=False)
    
    parser.add_argument('-g',
                        '--guion',
                        action="store_true",
                        help='Quitar guiones y saltos de linea',
                        default=False)
    
    return parser, parser.parse_args()