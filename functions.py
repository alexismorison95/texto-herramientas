import os



def resolver(input, output, justificado: bool, guion: bool):
    
    result = ""

    try:
        result = read_file(input)
    except FileNotFoundError:
        result = input
    
    print()

    if justificado:
        result = quitar_justificado(result)
        print('- Texto justificado')
    
    if guion:
        result = quitar_guiones(result)
        print('- Texto sin guiones ni salto de lineas')
    
    if output:
        save_file(output, result)
        print('- Resultado guardado en: {}'.format(output))
    else:
        print()
        print(result)


def quitar_justificado(texto: str):
    
    words = texto.split()
    text = ''

    for w in words:
        text += w + ' '
    
    return text


def quitar_guiones(texto: str):
    
    t = texto.split('\n')
    text = ''

    for line in t:
        aux = line.replace('-', '')
        text += aux + ' '
    
    return text


file_dir = os.path.dirname(os.path.realpath('__file__'))

def read_file(input_file: str):
    file_name = os.path.join(file_dir, input_file)

    with open(file_name, "r") as file:
        content = file.readlines()

        text = ''

        for l in content:
            text += l

        return text


def save_file(output_file: str, content: str):
    file_name = os.path.join(file_dir, output_file)

    with open(file_name, "a+") as file:
        file.write(content)