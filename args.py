from argparse import ArgumentParser
from argparse import FileType

from sys import stdin
from sys import stdout



def parseArgs():

    parser = ArgumentParser(description=__doc__)

    parser.add_argument('-f',
                        '--file',
                        help='Leer el texto desde un archivo',
                        type=FileType('r'),
                        default=stdin)

    parser.add_argument('-i',
                        '--input',
                        help='Leer el texto desde la consola',
                        type=str,
                        default=False)
    
    parser.add_argument('-s',
                        '--save',
                        help='Escribir resultado en un archivo',
                        type=FileType('w'),
                        default=stdout)
    
    parser.add_argument('-o',
                        '--output',
                        action="store_true",
                        help='Escribir resultado en la consola',
                        default=False)

    parser.add_argument('-j',
                        '--justificado',
                        action="store_true",
                        help='Quitar justificado.',
                        default=False)
    
    parser.add_argument('-g',
                        '--guion',
                        action="store_true",
                        help='Quitar guiones y saltos de linea.',
                        default=False)
    
    return parser, parser.parse_args()