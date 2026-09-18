import random

TAMANHO_TOTAL = 6
TAMANHO_UTIL = 4
LIMPO = 0
PAREDE = 1
SUJO = 2
MIN_SUJEIRAS = 3
MAX_SUJEIRAS = 7


def criar_sala(tamanho_total: int = TAMANHO_TOTAL) -> list[list[int]]:
    # Bordas (linha/coluna 1 e 6 do enunciado, índices 0 e tamanho_total-1 aqui) são parede;
    # só o quadrado interno (4x4) é sala limpável e recebe entre MIN_SUJEIRAS e MAX_SUJEIRAS sujeiras.
    sala = [[PAREDE] * tamanho_total for _ in range(tamanho_total)]
    celulas = [(l, c) for l in range(1, tamanho_total - 1) for c in range(1, tamanho_total - 1)]
    for l, c in celulas:
        sala[l][c] = LIMPO
    for l, c in random.sample(celulas, random.randint(MIN_SUJEIRAS, MAX_SUJEIRAS)):
        sala[l][c] = SUJO
    return sala


def checkObj(sala: list[list[int]]) -> int:
    # Usada pelo agente baseado em objetivos (próxima etapa): 1 = ainda há sujeira, 0 = sala limpa.
    return 1 if any(SUJO in linha for linha in sala) else 0
