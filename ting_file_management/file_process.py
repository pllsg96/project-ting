import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    if path_file not in instance.fila:
        instance.enqueue(path_file)

        print(file_info, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance.__len__():
        return print("Não há elementos", file=sys.stdout)
    path_file = instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
