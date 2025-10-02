# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral do Projeto

**AlfabetizeiAi** (anteriormente APEDC) é um Trabalho de Conclusão de Curso de Engenharia de Software desenvolvido no Uni-FACEF. O projeto consiste em um aplicativo educacional voltado para o ensino de crianças, focado em três categorias principais: Cálculos, Letras e Palavras, e Imagens.

**Importante**: Este repositório contém principalmente documentação, artefatos de projeto e protótipos. Não há código-fonte de implementação (Flutter, React Native, etc.) no momento.

## Estrutura do Repositório

```
├── Artigo/                    # Artigo científico do TCC em formato .docx e .pdf
│   └── Entrevista/           # Materiais de entrevista
├── Artefatos/                # Documentação e artefatos do projeto
│   ├── 5W1H/                 # Análise 5W1H
│   ├── Canvas/               # Business Model Canvas
│   ├── Cenario_de_Teste/     # Cenários e casos de teste
│   ├── Diagramas_UML/        # Diagramas de Caso de Uso e Classes
│   ├── Documentacao/         # Documentação de casos de uso (.xlsx)
│   └── EAP/                  # Estrutura Analítica do Projeto
└── Prototipo/                # Protótipos e assets
    ├── Assets/Images/        # Imagens organizadas por categoria e funcionalidade
    └── Funcional/            # Protótipo funcional em PDF
```

## Arquitetura do Aplicativo

O aplicativo está organizado em três categorias principais de jogos educacionais:

### 1. Cálculos
- **Adições**: Exercícios de soma
- **Subtrações**: Exercícios de subtração
- **Multiplicações**: Exercícios de multiplicação
- **Divisões**: Exercícios de divisão

### 2. Letras e Palavras
- **Letras**: Reconhecimento e aprendizado de letras
- **Palavras**: Formação e reconhecimento de palavras

### 3. Imagens
- **Objetos**: Identificação de objetos
- **Animais**: Identificação de animais

### Fluxo de Autenticação
O aplicativo possui sistema de login com:
- Login tradicional (usuário/senha)
- Login social (Google, Facebook, Apple ID)
- Cadastro inicial com aceite de termos de contrato

## Recursos Importantes

- **Protótipo Figma**: O design está disponível em [Figma Online](https://www.figma.com/file/TZR3CZQWU1AnDespexqltq/APEDC?node-id=0%3A1)
- **Assets**: Todas as imagens possuem licença Creative Commons
- **Diagramas UML**: Disponíveis em `Artefatos/Diagramas_UML/` (Caso de Uso e Classes)
- **Documentação de Casos de Uso**: Arquivo Excel em `Artefatos/Documentacao/Documentacao_de_Casos_de_Uso.xlsx`

## Trabalhando com este Repositório

### Documentação
- O artigo científico está em `Artigo/` em formatos .docx e .pdf
- Todos os artefatos de engenharia de software estão em `Artefatos/`
- As imagens do protótipo estão organizadas por funcionalidade em `Prototipo/Assets/Images/`

### Protótipo
- O protótipo funcional completo está em `Prototipo/Funcional/App.pdf`
- As imagens estão organizadas por categoria: Login, Contract_Terms, Home_and_Options, Categories

### Licença
Projeto sob licença MIT.
