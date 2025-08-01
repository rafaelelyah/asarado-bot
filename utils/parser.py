def parse_tags(message):
    print("🚀 Função parse_tags chamada")
    content = message.content.strip().upper()
    tags = []

    # Extrai a primeira linha da mensagem
    first_line = content.splitlines()[0].strip()

    # Verifica se começa com "!" e se a tag é válida
    if first_line.startswith("!"):
        tag = first_line[1:]
        if tag in {"MAJOR", "MINOR", "PATCH", "VERSION", "TASKS", "LOG"}:
            tags.append(tag)

    print(f"🔍 Tags encontradas: {tags}")
    return tags