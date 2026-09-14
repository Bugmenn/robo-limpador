def imprimir_grade(grade: list[list[bool]]) -> None:
    for linha in grade:
        print(" ".join("X" if suja else "." for suja in linha))
