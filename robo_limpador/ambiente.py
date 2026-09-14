import random

TAMANHO = 6
PROBABILIDADE_SUJEIRA = 0.3


class Ambiente:
    def __init__(self, tamanho: int = TAMANHO, probabilidade: float = PROBABILIDADE_SUJEIRA):
        self.tamanho = tamanho
        self.probabilidade = probabilidade
        self.grade = [[False] * tamanho for _ in range(tamanho)]

    def sortear_sujeira(self) -> None:
        for linha in range(self.tamanho):
            for coluna in range(self.tamanho):
                self.grade[linha][coluna] = random.random() < self.probabilidade
