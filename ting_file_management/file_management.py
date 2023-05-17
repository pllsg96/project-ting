import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.lower().endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return None

    try:
        allLines = []
        with open(path_file, 'r') as file:
            for eachLine in file:
                allLines.append(eachLine.rstrip('\n'))
        return allLines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None
