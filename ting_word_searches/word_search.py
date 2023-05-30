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
            result = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": []
            }
            for o in ocurr:
                conteudo = file_info["linhas_do_arquivo"][o["linha"] - 1]
                result["ocorrencias"].append({
                    "linha": o["linha"],
                    "conteudo": conteudo.rstrip()
                })
            occurrences.append(result)
    return occurrences
