# CLAUDE.md

Guia para o Claude Code ao trabalhar neste repositório.

## Estado do projeto

`robo-limpador` está em estágio inicial: ainda não há código-fonte, build, testes ou lint configurados. Antes de assumir stack ou comandos, verificar se já existem arquivos de configuração (package.json, requirements.txt, etc.) — se não existirem, perguntar ao usuário qual stack será usada.

## Estrutura atual

- `README.md` — placeholder
- `claude/` — clone do repositório https://github.com/Bugmenn/claude com skills, agentes e o prompt de setup (`config claude.md`) usados para configurar o Claude Code nesta máquina
- `Memory/` — memória do projeto (`diretrizes.md` + `robo-limpador.memory`), seguindo a Regra 00 do CLAUDE.md global

## Memória entre sessões

Antes de iniciar qualquer tarefa, ler `Memory/diretrizes.md` e `Memory/robo-limpador.memory`. Ao final de cada atividade, registrar o que foi feito em `Memory/robo-limpador.memory` na seção "Registro de Atividades Recentes".
