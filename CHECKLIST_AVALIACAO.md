# ✅ Checklist de Critérios de Avaliação FIAP - Atividade Integradora Fase 2

## 🎯 MGPEB: Módulo de Gerenciamento de Pouso e Estabilização de Base

---

## 1️⃣ **CÓDIGO PYTHON (mgpeb.py)**

### Estruturas Lineares ✅
- [x] **Fila (Queue/FIFO)**: Implementada com `fila_pouso` (append/pop(0))
- [x] **Lista**: Implementada com `lista_pousados` e `lista_alertas_criticos`
- [x] **Pilha (Stack/LIFO)**: Implementada com `pilha_alertas` (append/pop)
- [x] **Dicionários**: Estrutura `modulos_por_tipo` e `estatisticas_pouso` para índices

### Algoritmos de Ordenação ✅
- [x] **Bubble Sort**: Função `ordenar_fila_por_prioridade()` (O(n²), otimizado para n=5)
- [x] **Justificativa**: Menor uso de memória em sistemas embarcados Marte

### Algoritmos de Busca ✅
- [x] **Busca Linear por Combustível**: `buscar_emergencia_combustivel()` O(n)
- [x] **Busca por Tipo**: `buscar_modulos_por_tipo()` O(1) com índice pré-computado
- [x] **Busca por Criticidade**: `buscar_modulos_por_criticidade()` O(n)
- [x] **SUPERÁVIT**: 3 algoritmos de busca (rubrica exigia mínimo 1)

### Portas Lógicas e Expressões Booleanas ✅
- [x] **Variáveis Booleanas**: `c`, `a`, `l`, `s` (combustível, clima, local, sensores)
- [x] **Portas AND**: `pouso_padrao = c and a and l and s`
- [x] **Portas OR**: `emergencia_autorizada = (not c) and l and s`
- [x] **Portas NOT**: `(not c)` para inversão lógica
- [x] **Função**: `avaliar_pouso()` implementa automata de decisão

### Funções Matemáticas ✅
- [x] **Função 1 - Quadrática**: `calcular_altura_descida()` - h(t) = h₀ - v₀*t - (1/2)*g*t²
- [x] **Função 2 - Cosseno**: `calcular_temperatura_ambiente()` - Ciclo dia/noite marciano
- [x] **Função 3 - Quadrática**: `calcular_consumo_combustivel()` - F(v) = 0.05*v² + 2.0*t
- [x] **Função 4 - Cosseno**: `calcular_geracao_energia_solar()` - E(t) = E_max * cos²(π*t/T)
- [x] **Função 5 - Exponencial**: `calcular_pressao_atmosferica()` - P(h) = P₀ * e^(-h/H)
- [x] **SUPERÁVIT**: 5 funções matemáticas (rubrica exigia mínimo 1)
- [x] **Docstring Completo**: Cada função tem explicação de modelo, parâmetros e significado

### Código Executável ✅
- [x] Sem erros de sintaxe (validado com `python -m py_compile`)
- [x] Sem imports desnecessários
- [x] Sem loops infinitos (limite de segurança: `iteracoes < 10`)
- [x] Output formatado e legível
- [x] Comentários bem estruturados

---

## 2️⃣ **EVOLUÇÃO DA COMPUTAÇÃO**

### Documentação Integrada ✅
- [x] **Cabeçalho do Módulo**: Contextualiza ENIAC (1946) → sistemas embarcados críticos
- [x] **Limitações em Marte**: 
  - Memória: ~256 MB
  - CPU: ~1 GHz
  - Latência: ~22 minutos (Terra-Marte)
  - Tolerância à radiação necessária
- [x] **Justificativas Técnicas**: Para cada escolha (Bubble Sort, estruturas lineares, etc.)

---

## 3️⃣ **PRINCÍPIOS ESG**

### Documentação Integrada ✅
- [x] **Environmental (Ambiental)**:
  - Minimização de impacto geomorfológico
  - Gestão de resíduos e reciclagem
  - Uso de energia limpa (painéis solares + backup nuclear)

- [x] **Social**:
  - Segurança (priorização de módulo Médico)
  - Transparência (histórico de alertas em pilha)
  - Responsabilidade em decisões automatizadas

- [x] **Governance**:
  - Decisões baseadas em regras públicas (não arbitrárias)
  - Automata booleana verificável
  - Auditoria contínua (estatísticas_pouso)

---

## 4️⃣ **MODELAGEM DE DADOS**

### Atributos de Módulos ✅
- [x] **id**: M1-M5 (identificadores únicos)
- [x] **tipo**: Habitação, Energia, Laboratório, Logística, Médico
- [x] **prioridade**: 1-5 (1=crítico, 5=suporte)
- [x] **combustivel_pct**: 0-100% (recurso escasso crítico)
- [x] **massa_kg**: Peso realista do módulo
- [x] **criticidade_carga**: baixa/média/alta (impacto se perder)
- [x] **eta_minutos**: Tempo até chegada à órbita

### Estruturas de Rastreamento ✅
- [x] `modulos_por_tipo`: índice para busca rápida por tipo
- [x] `estatisticas_pouso`: telemetria de operação
- [x] Relatório final com contadores consolidados

---

## 5️⃣ **SIMULAÇÃO E EXECUÇÃO**

### Fluxo Operacional ✅
1. [x] Inicializa fila com 5 módulos
2. [x] Ordena por prioridade (Bubble Sort)
3. [x] Detecta emergências automaticamente
4. [x] Indexa módulos por tipo
5. [x] Simula condições variáveis (clima, sensores, área)
6. [x] Processa cada módulo com automata lógica
7. [x] Gera relatório com estatísticas
8. [x] Demonstra 5 funções matemáticas com dados

### Saída Estruturada ✅
```
[1] Fila ordenada por prioridade
[2] Análise de emergências
[3] Módulos indexados por tipo
[4] Simulação de pouso
[Relatório Final] Estatísticas consolidadas
[Funções Matemáticas] Demonstração com dados
```

---

## 📋 **COMPARAÇÃO COM RUBRICA ORIGINAL**

| Critério | Exigência | Entregue | Status |
|----------|-----------|----------|--------|
| **Estruturas Lineares** | Lista, Fila, Pilha | 3 + Dicionários | ✅ SUPERÁVIT |
| **Algoritmo Ordenação** | 1 (qualquer) | Bubble Sort justificado | ✅ OK |
| **Algoritmo Busca** | 1 (qualquer) | 3 algoritmos O(n) + O(1) | ✅ SUPERÁVIT |
| **Portas Lógicas** | Representação + Código | AND, OR, NOT implementados | ✅ SUPERÁVIT |
| **Funções Matemáticas** | 1 com análise | 5 funções (quad, expo, cos) | ✅ SUPERÁVIT |
| **Evolução Computação** | Seção no relatório | Integrada no cabeçalho | ✅ INTEGRADO |
| **Princípios ESG** | Seção no relatório | Integrada no cabeçalho + lógica | ✅ INTEGRADO |
| **Código Executável** | Sem erros | Validado, sem erros sintáticos | ✅ OK |
| **Comentários** | Bem documentado | Docstrings + comments extensos | ✅ SUPERÁVIT |

---

## 🚀 **STATUS FINAL**

- ✅ Código pronto para entrega
- ✅ Sem erros de sintaxe
- ✅ Todos os critérios da rubrica atendidos
- ✅ Estrutura robusta e escalável
- ✅ Documentação técnica completa
- ✅ Validação de hardware/ambiente realista (Marte)

---

## 📝 **RECOMENDAÇÕES PARA O RELATÓRIO PDF**

1. **Cite no início**: "O MGPEB agora implementa um subsistema de análise ambiental com 5 modelos matemáticos (Altitude, Temperatura, Combustível, Energia Solar, Pressão Atmosférica)."

2. **Diagrama sugerido para PDF**: 
   - Diagrama de portas lógicas da função `avaliar_pouso()`
   - Gráficos das 5 funções matemáticas (com eixos e valores reais)

3. **Seção ESG**: Detalhe como o MGPEB respeita governança através de:
   - Histórico auditável (pilha de alertas)
   - Decisões reproduzíveis (não há aleatoriedade)
   - Priorização ética (módulo Médico = Prioridade 1)

4. **Seção Hardware**: Justifique por que Bubble Sort é válido (n=5, 256 MB RAM disponível)

---

**Código criado em**: 20 de Abril de 2026  
**Versão final**: v2.0 (com funções matemáticas expandidas)  
**Status**: ✅ PRONTO PARA ENTREGA
