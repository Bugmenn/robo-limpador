from robo_limpador.ambiente import Ambiente
from robo_limpador.visualizacao import imprimir_grade


def executar(numero_rodadas: int) -> None:
    ambiente = Ambiente()
    for rodada in range(1, numero_rodadas + 1):
        ambiente.sortear_sujeira()
        print(f"--- Rodada {rodada} ---")
        imprimir_grade(ambiente.grade)
        print()
