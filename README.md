# 🚀 Missão Aurora Siger - MGPEB

## Módulo de Gerenciamento de Pouso e Estabilização de Base
**Atividade Integradora - Fase 2 FIAP**

---

## 📂 Arquivos Principais

| Arquivo | Descrição |
|---------|-----------|
| **mgpeb.py** | 📌 Código-fonte (400+ linhas, 5 functions, completo) |
| **CHECKLIST_AVALIACAO.md** | 📋 Mapeamento com rubrica FIAP (confirmação de requisitos) |
| **GUIA_RELATORIO_PDF.md** | 📄 Template de 10 páginas para relatório técnico |
| **README.md** | Este arquivo |

---

## 🎯 O que foi Entregue

✅ **Código Fonte**
- 5 estruturas lineares (Fila, Listas, Pilha, Dicionários)
- 1 algoritmo de ordenação (Bubble Sort O(n²))
- 4+ algoritmos de busca (Combustível, Tipo, Criticidade)
- 5 funções matemáticas (Altura, Temp, Combustível, Energia, Pressão)
- Portas lógicas implementadas (AND, OR, NOT)
- Automata booleano para decisão de pouso
- Simulação realista com 5 módulos
- Relatório integrado com estatísticas

✅ **Documentação**
- Docstrings em toda função
- Contexto histórico (ENIAC → Marte)
- Princípios ESG integrados
- Justificativas arquiteturais

✅ **Validação**
- Sem erros de sintaxe
- Executa sem exceções
- Output formatado
- 5 commits semânticos no git

---

## 📊 Análise Rápida de Requisitos

| Critério | Exigência | Entregue | Status |
|----------|-----------|----------|--------|
| Estruturas Lineares | 3 | 4 (Fila, Listas, Pilha, Dicts) | ✅ SUPERÁVIT |
| Ordenação | 1 | Bubble Sort justificado | ✅ OK |
| Busca | 1 | 4 algoritmos | ✅ SUPERÁVIT |
| Portas Lógicas | Sim | AND, OR, NOT completo | ✅ OK |
| Funções Matemáticas | 1 | 5 funções diferentes | ✅ SUPERÁVIT |
| Evolução Computação | Seção | Integrada no código | ✅ OK |
| ESG | Seção | Integrada + lógica | ✅ OK |
| Execução | Sem erros | Validado | ✅ OK |

---

## 🔬 As 5 Funções Matemáticas

1. **Altura(t)** = h₀ - v₀·t - ½·g·t² (Quadrática)
2. **Temperatura(t)** = T_min + ΔT·cos(2π·t/24.65) (Cosseno)
3. **Combustível(v)** = 0.05·v² + 2.0·t (Quadrática)
4. **Energia(t)** = E_max·cos²(π·t/24.65) (Cosseno²)
5. **Pressão(h)** = P₀·e^(-h/H) (Exponencial)

Cada função é modelada para fenômenos reais em Marte.

---

## 🏗️ Arquitetura Técnica

```
ENTRADA: 5 módulos (M1-M5)
    ↓
PROCESSAMENTO:
├── Ordenação por prioridade
├── Busca de emergências
├── Indexação por tipo
└── Avaliação com portas lógicas
    ↓
SAÍDA: Relatório com decisões
```

---

## ⚙️ Hardware em Marte vs Terra

| Recurso | Terra | Marte/MGPEB | Impacto |
|---------|-------|------------|--------|
| CPU | ~3.5 GHz | ~1 GHz | Bubble Sort ainda é rápido |
| RAM | ~8 GB | ~256 MB | Estruturas lineares (não árvores) |
| Latência | <1 ms | ~22 min | Decisões autônomas críticas |

---

## 🎓 Conceitos Aplicados

- ✅ Classes de complexidade (O(1), O(n), O(n²))
- ✅ Estruturas de dados lineares (ADTs)
- ✅ Algoritmos clássicos (Ordenação, Busca)
- ✅ Lógica booleana (Portas lógicas)
- ✅ Funções matemáticas (Polinomiais, Trigonométricas, Exponenciais)
- ✅ Computação embarcada (Restrições de hardware)
- ✅ Governança ESG (Transparência, Auditoria)
- ✅ Contexto histórico (ENIAC 1946 → MGPEB 2026)

---

## 📋 Como Usar

### Executar o Código
```bash
cd /workspaces/Missao-Aurora-Siger
python mgpeb.py
```

### Validar Sintaxe
```bash
python -m py_compile mgpeb.py
```

### Ver Histórico Git
```bash
git log --oneline
```

---

## 📚 Documentação Adicional

- **CHECKLIST_AVALIACAO.md** → Mapeamento com rubrica (✅/❌ para cada critério)
- **GUIA_RELATORIO_PDF.md** → Template estruturado para relatório técnico de 10 páginas

---

## 🌍 Contexto: Evolução da Computação

| Ano | Evento | Lição para MGPEB |
|-----|--------|-----------------|
| 1946 | ENIAC (primeiro computador propósito geral) | Viabilidade de automação |
| 1962 | Apollo GC (navegação na Lua) | Sistemas críticos funcionam com poucos KB |
| 2020 | Perseverance (rover em Marte) | Hardware embarcado com tolerância a radiação |
| 2026 | MGPEB (colônia Aurora) | Eficiência + Transparência + Governança ESG |

---

## 🎯 Próximas Etapas

1. Desenvolver **Relatório PDF** (5-10 páginas)
   - Use template em GUIA_RELATORIO_PDF.md
   
2. Criar **Anexo de Estruturas de Dados**
   - Detalhar cada EDL com exemplos
   
3. Preparar **Apresentação** (se houver)
   - Demo do código
   - Discussão sobre ESG + tecnologia

---

## ✅ Status de Entrega

- ✅ Código completo e testado
- ✅ Sem erros de sintaxe/runtime
- ✅ Documentação integrada
- ✅ Documentação auxiliar (guides)
- ✅ Sincronizado com GitHub
- ✅ Histórico de commits semântico

**Status:** 🟢 Pronto para Avaliação

---

## 📞 Informações

- **Integrante:** Maria Eduarda Fernandes de Oliveira
- **Instituição:** FIAP
- **Data de Criação:** 20 de Abril de 2026
- **Repositório:** https://github.com/ByLumery/Missao-Aurora-Siger

---

*Última atualização: 20 de Abril de 2026*
