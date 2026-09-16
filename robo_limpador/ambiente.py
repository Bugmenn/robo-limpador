import random

TAMANHO = 4
PROBABILIDADE_SUJEIRA = 0.3


def criar_sala(tamanho: int = TAMANHO, probabilidade: float = PROBABILIDADE_SUJEIRA) -> list[list[int]]:
    return [
        [1 if random.random() < probabilidade else 0 for _ in range(tamanho)]
        for _ in range(tamanho)
    ]


def checkObj(sala: list[list[int]]) -> int:
    # Usada pelo agente baseado em objetivos (próxima etapa): 1 = ainda há sujeira, 0 = sala limpa.
    return 1 if any(1 in linha for linha in sala) else 0
