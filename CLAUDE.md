# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sobre o projeto

Atividade avaliativa de IA: um agente Aspirador de Pó Automático (APA), implementado em duas etapas — primeiro como **Agente Reativo Simples**, depois evoluído para **Agente Baseado em Objetivos**. O enunciado oficial está em `docs/AspiradorDePó.pdf` — é a fonte da verdade para requisitos (nomes de função exigidos, assinaturas, regras).

**Mundo real: matriz 6x6 com bordas-parede.** Linha 1, linha 6, coluna 1 e coluna 6 (1-indexado) são paredes; a sala limpável é o quadrado 4x4 central. Representado numa única matriz com `LIMPO=0`, `PAREDE=1`, `SUJO=2`. Cada sala tem de 3 a 7 sujeiras (`MIN_SUJEIRAS`/`MAX_SUJEIRAS`).

**Etapa atual do código: só o ambiente (matriz 4x4 com sujeira sorteada).** A lógica do agente (`agenteReativoSimples`, `agenteObjetivo`, `funcaoMapear`, `checkObj` sendo consumida, contador `pontos`) ainda não foi implementada — checklist detalhado em `PROXIMOS_PASSOS.md`.

## Comandos

```bash
python -m venv .venv                          # criar o ambiente virtual (uma vez)
.venv/Scripts/python.exe -m pip install -r requirements.txt   # instalar numpy + matplotlib
.venv/Scripts/python.exe main.py               # rodar (abre janela do matplotlib com a matriz)
```

Sem testes, lint ou build configurados.

## Arquitetura

- `robo_limpador/ambiente.py` — `criar_sala(tamanho_total=6)`: gera a matriz 6x6 (borda=`PAREDE`(1), interno 4x4=`SUJO`(2)/`LIMPO`(0), com 3 a 7 células sujas sorteadas via `random.sample`), sorteada uma vez por episódio (não re-sorteia a cada passo). `checkObj(sala)`: retorna `1`/`0` conforme há `SUJO` na matriz (atenção: o `1` retornado é o sinal "há sujeira", não o valor de célula `PAREDE`) — já existe aqui porque o enunciado pede essa função fora do agente, mas só terá consumidor quando o agente for implementado.
- `robo_limpador/visualizacao.py` — `exibir(matriz, pos_x=None, pos_y=None)`: exibe a matriz com `matplotlib`, adaptado do modelo de código fornecido no enunciado. `pos_x`/`pos_y` são opcionais porque ainda não há agente com posição.
- `main.py` — cria a sala e chama `exibir()`.

Ao adicionar o agente: manter a direção de dependência atual (agente consome `ambiente`, não o contrário) e reaproveitar `criar_sala`/`checkObj`/`exibir` em vez de duplicar lógica.

## Memória entre sessões

Antes de iniciar qualquer tarefa, ler `Memory/diretrizes.md` e `Memory/robo-limpador.memory` — este último tem o histórico de decisões (por que a simulação genérica 6x6 anterior foi descartada, o que ficou de fora nesta etapa, resultado das revisões de arquitetura/otimização já feitas). Ao final de cada atividade, registrar o que foi feito em `Memory/robo-limpador.memory` na seção "Registro de Atividades Recentes".

## Outras pastas

- `docs/AspiradorDePó.pdf` — enunciado oficial da atividade avaliativa.
- `PROXIMOS_PASSOS.md` — checklist detalhado do que falta implementar (agente reativo simples, agente baseado em objetivos, `RESPOSTAS.md`).
- `claude/` — clone do repositório https://github.com/Bugmenn/claude (fonte original das skills/agentes abaixo), mantido como pasta comum, sem `.git` interno.
- `.claude/skills/` — `arquitetura-projeto`, `otimizacao-codigo`, `frontend-design`.
- `.claude/agents/` — `depurador`, `descritor-pr`, `documentador`, `especialista-banco`, `revisor-codigo`.
