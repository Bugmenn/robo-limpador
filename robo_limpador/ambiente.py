import random

TAMANHO_TOTAL = 6
TAMANHO_UTIL = 4
PAREDE = -1
PROBABILIDADE_SUJEIRA = 0.3


def criar_sala(tamanho_total: int = TAMANHO_TOTAL, probabilidade: float = PROBABILIDADE_SUJEIRA) -> list[list[int]]:
    # Bordas (linha/coluna 1 e 6 do enunciado, índices 0 e tamanho_total-1 aqui) são parede;
    # só o quadrado interno (4x4) é sala limpável e recebe sujeira sorteada.
    sala = [[PAREDE] * tamanho_total for _ in range(tamanho_total)]
    for linha in range(1, tamanho_total - 1):
        for coluna in range(1, tamanho_total - 1):
            sala[linha][coluna] = 1 if random.random() < probabilidade else 0
    return sala


def checkObj(sala: list[list[int]]) -> int:
    # Usada pelo agente baseado em objetivos (próxima etapa): 1 = ainda há sujeira, 0 = sala limpa.
    return 1 if any(1 in linha for linha in sala) else 0
