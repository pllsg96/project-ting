def exists_word(word, instance):
    result = []
    while not instance.__len__:
        file = instance.enqueue()
        occurrences = []
        with open(file, 'r') as f:
            lines = f.readlines()
            for line_number, line in enumerate(lines, start=1):
                if word.lower() in line.lower():
                    occurrences.append({"linha": line_number})
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file,
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
