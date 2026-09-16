# Próximos passos — Atividade Avaliativa (APA)

Este documento registra o que **ainda falta implementar** da atividade avaliativa (enunciado completo em `docs/AspiradorDePó.pdf`), já que a etapa atual do código cobriu só o ambiente (matriz 4x4 + visualização). Serve de checklist para retomar o trabalho depois.

## O que já existe

- `robo_limpador/ambiente.py` — `criar_sala(tamanho=4, probabilidade=0.3)` (matriz 4x4, sujeira sorteada uma vez) e `checkObj(sala)` (`1` se há sujeira, `0` se limpa — já pronta, só falta ser consumida pelo agente).
- `robo_limpador/visualizacao.py` — `exibir(matriz, pos_x=None, pos_y=None)`, adaptado do modelo de código do enunciado (matplotlib).
- `main.py` — só cria a sala e chama `exibir()`, sem agente.

## Parte 1 — Agente Reativo Simples (pendente)

Criar `robo_limpador/agente.py` com:

- **`funcaoMapear(percepcao)`** — dica do enunciado: função central que decide a ação a partir da percepção. Deve concentrar a lógica "se a célula atual está suja → `'aspirar'`; senão → próximo passo de um percurso que garanta cobrir toda a sala".
- **`agenteReativoSimples(percepcao)`** — retorna uma de 5 ações: `'acima'`, `'abaixo'`, `'esquerda'`, `'direita'`, `'aspirar'`. Precisa garantir limpar toda a sala **independentemente da posição inicial**. Ações contra a parede não têm efeito (mas não são proibidas — não precisa impedir de tentar).
- Como um agente puramente reativo (sem estado) não consegue garantir cobertura total por definição, a prática usual (e compatível com o modelo do enunciado, que já usa `posAPAx`/`posAPAy` como globais) é manter um pequeno estado global mínimo (posição atual + direção do percurso) para implementar uma varredura sistemática tipo zigue-zague (boustrophedon), que cobre todas as células a partir de qualquer ponto de partida.
- **Pergunta a responder (documentar em `RESPOSTAS.md`, ver abaixo):** essa solução é extensível para um mundo 3x3? E para 6x6? Por quê.

## Parte 2 — Agente Baseado em Objetivos (pendente)

Ainda em `robo_limpador/agente.py`:

- **`agenteObjetivo(percepcao, objObtido)`** — retorna uma de 6 ações (as 5 anteriores + `'NoOp'`). `objObtido` é a saída de `checkObj(sala)` (já implementada em `ambiente.py`). Quando `objObtido == 0` (sala limpa), a ação vira `'NoOp'`.
- Agente começa no quadrado (1,1) — atenção ao mapeamento entre a notação 1-indexada do enunciado e os índices 0-indexados da matriz em Python (documentar essa conversão em comentário no código).
- Variável contador **`pontos`** — conta o número de passos até atingir o objetivo (sala limpa).
- Reaproveitar a mesma lógica de `funcaoMapear`/varredura da Parte 1, só adicionando o contador e a checagem de objetivo.
- **Pergunta a responder (documentar em `RESPOSTAS.md`):** é possível ter todo o espaço efetivamente limpo? Justificar.

## Visualização (ajuste pendente quando o agente existir)

`exibir()` já aceita `pos_x`/`pos_y` opcionais — quando o agente for implementado, passar a posição real do agente a cada passo do loop de simulação para o marcador aparecer sobre a matriz. Vale considerar `plt.clf()` entre chamadas (já presente no modelo do enunciado) para não acumular figuras quando isso virar um loop.

## `RESPOSTAS.md` (a criar)

Arquivo separado na raiz do projeto com as duas respostas discursivas do enunciado (uma por parte, ver acima), cada uma justificada — só faz sentido escrever depois que a lógica do agente estiver implementada e puder embasar a justificativa.

## Main / loop de simulação (a criar)

`main.py` também precisa ganhar (ou um novo módulo `simulacao.py`) o loop que:
1. Cria a sala e posiciona o agente.
2. A cada passo, monta a `percepcao`, chama `agenteReativoSimples` (Parte 1) ou `agenteObjetivo` + `checkObj` (Parte 2), aplica a ação (move a posição ou zera a célula se `'aspirar'`), chama `exibir()`.
3. Para a Parte 2, imprime `pontos` ao final e confirma que a última ação foi `'NoOp'`.
