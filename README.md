# 🚀 Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
**Missão Aurora Siger - Fase 2 de Colonização Marciana**

Este repositório contém a entrega final da **Fase 2 da Atividade Integradora** do curso da FIAP. O projeto simula o sistema de software embarcado responsável por organizar, priorizar e autorizar o pouso de módulos vitais em uma colônia nascente em Marte, respeitando restrições extremas de hardware, clima e recursos.

## 📋 Sobre o Projeto

O **MGPEB** atua como o cérebro da operação de aproximação. Para simular as limitações reais de uma missão espacial (como a alta radiação que afeta a memória e o processamento), o sistema foi construído exclusivamente com programação procedural rigorosa, dispensando o uso de bibliotecas pesadas e optando por algoritmos de baixa complexidade espacial.

### 🛠️ Tecnologias e Conceitos Aplicados:
- **Estruturas de Dados Lineares:** - `Fila (Queue/FIFO)` para a ordem padrão de aproximação orbital.
  - `Pilha (Stack/LIFO)` para o empilhamento e tratamento de alertas críticos.
  - `Lista (List)` para o registro histórico de módulos pousados com sucesso.
- **Algoritmos:** - `Bubble Sort` (Ordenação por criticidade/prioridade do módulo).
  - `Busca Linear` (Filtros de emergência de combustível e tipo de módulo).
- **Lógica Booleana:** Uso de portas lógicas (`AND`, `OR`, `NOT`) para determinar a autorização de pouso baseada em telemetria (Combustível, Clima, Área Livre e Sensores).
- **Modelagem Matemática:** Implementação de função quadrática ($h(t) = h_0 - v_0t - \frac{1}{2}gt^2$) para cálculo e controle da altitude durante a frenagem com retrofoguetes.
- **Governança Espacial:** Aplicação de diretrizes **ESG** (Environmental, Social, and Governance) na tomada de decisão automatizada, priorizando vidas humanas (Módulo Médico) e proteção planetária.

## 📂 Estrutura do Repositório

- 📄 `mgpeb.py`: Código-fonte executável do protótipo do sistema em Python.
- 📕 `Relatório_MGPEB.pdf`: Documentação técnica completa contendo:
  - Descrição do cenário.
  - Diagramas do circuito lógico de decisão.
  - Análise qualitativa da modelagem matemática.
  - Ensaio sobre a evolução computacional e a aplicação de ESG em Marte.

## ⚙️ Como Executar a Simulação

Certifique-se de ter o [Python 3.x](https://www.python.org/downloads/) instalado em sua máquina.

1. Clone o repositório ou baixe os arquivos.
2. Abra o terminal no diretório do projeto.
3. Execute o script com o comando:
   ```bash
   python mgpeb.py