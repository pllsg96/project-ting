from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    occurrences = []
    if not instance.__len__():
        return None

    for file in instance.fila:
        file_processing = txt_importer(file)
        file_info = {
            "nome_do_arquivo": file,
            "qtd_linhas": len(file_processing),
            "linhas_do_arquivo": file_processing
        }
        ocurr = [
            {"linha": i}
            for i, lines in enumerate(file_info["linhas_do_arquivo"], 1)
            if word.lower() in lines.lower()
        ]

        if ocurr:
            occurrences.append({
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": ocurr
            })
    return occurrences


def search_by_word(word, instance):
    result = []
    while not instance.__len__():
        # file = instance.dequeue()
        # occurrences = []
        # with open(file, 'r') as f:
        #     lines = f.readlines()
        #     for line_number, line in enumerate(lines, start=1):
        #         if word.lower() in line.lower():
        #             occurrences.append({
        #                 "linha": line_number,
        #                 "conteudo": line.strip()
        #             })
        # if occurrences:
        #     result.append({
        #         "palavra": word,
        #         "arquivo": file,
        #         "ocorrencias": occurrences
        #     })
        return True
    return result
