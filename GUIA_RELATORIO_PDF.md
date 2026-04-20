# 📋 Recomendações para Relatório Técnico em PDF

## Estrutura Sugerida do Relatório (5-10 páginas)

---

## PÁGINA 1: CAPA
```
ATIVIDADE INTEGRADORA – FASE 2
Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
Missão Aurora Siger

Integrante: Maria Eduarda Fernandes de Oliveira
Data: Abril de 2026
Instituição: FIAP
```

---

## PÁGINA 2: SUMÁRIO EXECUTIVO

**O que escrever:**
- O MGPEB é um sistema de controle de pouso modular para colônia em Marte
- Implementa 5 algoritmos: 1 ordenação (Bubble Sort), 3+ buscas (combustível, tipo, criticidade)
- Inclui subsistema de análise ambiental com 5 modelos matemáticos físicos
- Prioriza segurança, transparência e sustentabilidade (ESG)
- Designed para ambientes embarcados com restrições de memória e processamento

---

## PÁGINA 3: DESCRIÇÃO DO CENÁRIO

### Contexto
Escreva:
> A Aurora Siger é uma colônia nascente em Marte que requer um sistema automatizado de controle de pouso para módulos especializados. Cada módulo (Habitação, Energia, Laboratório, Logística, Médico) é crítico e deve pousar em uma sequência otimizada respeitando:
> - Nível de combustível restante
> - Criticidade da carga
> - Prioridade de entrada em operação
> - Condições atmosféricas e de superfície

### Módulos do Sistema
Crie uma tabela:

| ID | Tipo | Prioridade | Combustível | Massa | Criticidade | ETA |
|----|------|-----------|-------------|-------|-------------|-----|
| M5 | Médico | 1 (crítica) | 10% | 2200 kg | Alta | 15 min |
| M2 | Energia | 2 | 60% | 3200 kg | Alta | 18 min |
| M1 | Habitação | 3 | 80% | 4500 kg | Média | 25 min |
| M3 | Laboratório | 4 | 90% | 2800 kg | Média | 32 min |
| M4 | Logística | 5 (suporte) | 70% | 5100 kg | Baixa | 40 min |

**Análise:**
- Módulo M5 (Médico) tem prioridade 1 apesar de combustível crítico → decisão ética ESG
- Distribuição de massa realista (~18 toneladas totais)
- Intervalo de ETA simula cenário realista de múltiplos lançadores

---

## PÁGINA 4: REGRAS DE DECISÃO COM PORTAS LÓGICAS

### 4.1 Diagrama de Decisão

Inclua um diagrama ASCII ou visual:

```
┌─────────────────────────────────────────────────────────────┐
│                   AVALIAÇÃO DE POUSO                        │
│                                                              │
│  c = (combustível ≥ 20%)    [>=]                            │
│  a = clima adequado          [ok]          ┌─────┐          │
│  l = área livre              [ok]    ──┬───┤ AND ├──→ [OK]  │
│  s = sensores ok             [ok]    ──┤   └─────┘   [PAD]  │
│                              [ok]    ──┬───────────────────│
│  ¬c = NOT(combustível ≥ 20%) [emergency]               │
│                                ┌──┬───┤ AND ├──→ [OK]       │
│                          ┌─────┘  │   └─────┘  [EMERG]     │
│                          │  ┌──┐  │                         │
│                          └──┤ X ├──┴────→ [NEGADO]         │
│                             └──┘                           │
└─────────────────────────────────────────────────────────────┘

LEGENDA:
  [>=]   = Avalia combustível acima do limite crítico (20%)
  [ok]   = Condição atendida (Verdadeiro)
  ¬      = Operador NOT (negação)
  AND    = Operador AND (conjunção lógica)
  [PAD]  = Pouso Padrão (condições ideais)
  [EMERG]= Pouso Emergência (sem clima, com área livre)
  [X]    = Bloqueio lógico (rejeita pouso)
```

### 4.2 Expressões Booleanas

**Pouso Padrão (AUTORIZADO):**
```
P = c ∧ a ∧ l ∧ s
(combustível OK) AND (clima OK) AND (área livre) AND (sensores OK)
```

**Pouso Emergência (AUTORIZADO COM ALERTA):**
```
E = ¬c ∧ l ∧ s
NOT(combustível OK) AND (área livre) AND (sensores OK)
Requer modulação de clima para pousar (maior risco)
```

**Pouso Negado (ABORTADO):**
```
N = ¬(P ∨ E)
Qualquer outra combinação resulta em falha de autorização
```

---

## PÁGINA 5: FUNÇÕES MATEMÁTICAS

### 5.1 Função 1: Altura em Função do Tempo (Quadrática)

**Fórmula:**
$$h(t) = h_0 - v_0 \cdot t - \frac{1}{2} g \cdot t^2$$

**Parâmetros:**
- $h_0$ = altura inicial em km (tipicamente 50-100 km)
- $v_0$ = velocidade inicial de descida em km/s
- $g$ = aceleração de Marte = 3.71 m/s² = 0.003711 km/s²
- $t$ = tempo em segundos

**Significado:**
A função é quadrática com $t^2$ negativo, modelando uma parábola invertida. Quanto mais tempo passa:
- Altura diminui linearmente com $v_0 \cdot t$ (queda por inércia)
- Altura diminui ainda mais com $\frac{1}{2}g \cdot t^2$ (aceleração gravitacional)

**Aplicação ao MGPEB:**
Ajustando retrofoguetes, reduz-se $v_0$ para que h(200s) atinja 0 (solo) em lugar seguro.

**Gráfico sugerido:**
```
Altura (km)
50 |     •
40 |    /
30 |   /
20 |  /
10 | /•
 0 |_______________
   0  50 100 150 200  (tempo em segundos)
```

---

### 5.2 Função 2: Temperatura Ambiente (Cosseno)

**Fórmula:**
$$T(t) = T_{noite} + (T_{dia} - T_{noite}) \cdot \left[ 0.5 + 0.5 \cos\left( 2\pi \cdot \frac{t}{24.65} \right) \right]$$

**Parâmetros:**
- $T_{dia}$ = 250 K ≈ -23°C (máximo solar ao meio-dia)
- $T_{noite}$ = 130 K ≈ -143°C (mínimo durante noite)
- $t$ = hora local (0-24.65 horas = 1 dia marciano)
- Período = 24.65 horas (dia marciano é 3% mais longo que terrestre)

**Significado:**
Oscilação cíclica e contínua. O cosseno varia de -1 a +1:
- Quando $\cos(\ldots) = 1$ → T = $T_{dia}$ (meio-dia)
- Quando $\cos(\ldots) = -1$ → T = $T_{noite}$ (meia-noite)

**Aplicação ao MGPEB:**
Pousos programados preferencialmente durante o dia para:
- Maximizar energia solar nos painéis
- Reduzir consumo de aquecimento
- Melhorar eficiência de operações iniciais

**Gráfico sugerido:**
```
Temperatura (°C)
-20  |•                    •
-60  |  \                /
-100 |    \            /
-140 |      •        •
-180 |________________
     0  6 12 18 24  (horas marcianas)
```

---

### 5.3 Função 3: Consumo de Combustível (Quadrática)

**Fórmula:**
$$F(v) = 0.05 \cdot v^2 + 2.0 \cdot t$$

**Parâmetros:**
- $v$ = velocidade de descida em m/s
- $t$ = tempo de ativação de retrofoguetes em segundos
- Coeficientes: 0.05 (quadrático) e 2.0 (linear) ajustados para Marte

**Significado:**
Modelo quadrático em relação à velocidade reflete aumento não-linear de consumo:
- Dobrar velocidade = quadrupla o consumo por retrofoguetes
- Aumentar tempo de retrofoguete = consumo proporcional

**Aplicação ao MGPEB:**
Trade-off crítico:
- Descida muito rápida ($v$ alto) = gasta muito combustível
- Descida muito lenta = mais tempo = também gasta combustível
- Ótimo em ~10-15 m/s para Marte (diferente da Terra: ~6 m/s)

**Exemplo de cálculo:**
- $v = 10$ m/s, $t = 100$ s → $F = 0.05(100) + 2(100) = 5 + 200 = 205\%$ 
- (Seria 100% máx, então necessita otimização de trajetória)

---

### 5.4 Função 4: Energia Solar (Cosseno Quadrado)

**Fórmula:**
$$E(t) = E_{max} \cdot \cos^2\left( \pi \cdot \frac{t}{24.65} \right)$$

**Parâmetros:**
- $E_{max}$ = potência máxima dos painéis em kW (tipicamente 5-10 kW)
- $t$ = hora local
- Período = 24.65 horas (dia marciano)

**Significado:**
Função cosseno ao quadrado:
- Sempre ≥ 0 (nunca negativa, energia não pode ser negativa)
- Máximo = 1.0 ao meio-dia ($\cos(0) = 1$ → $\cos^2(0) = 1$)
- Mínimo = 0 ao amanhecer/anoitecer ($\cos(\pi/2) = 0$)
- Muito mais zero à noite que seno puro (melhor modelo realista)

**Aplicação ao MGPEB:**
Define janela de recarregamento de baterias:
- Semestre em Marte com padrão de energia ≥ 0.8*$E_{max}$ dura ~6 horas
- Módulos de alta demanda (M2=Energia) devem pousar próximo ao meio-dia

---

### 5.5 Função 5: Pressão Atmosférica (Exponencial Decrescente)

**Fórmula:**
$$P(h) = P_0 \cdot e^{-h/H}$$

**Parâmetros:**
- $P_0$ = pressão ao nível do solo ≈ 600 Pa (1.6% da pressão terrestre)
- $h$ = altitude em km
- $H$ = altura de escala ≈ 11.1 km (escala onde P cai para P₀/e)

**Significado:**
Exponencial decrescente:
- A cada 11.1 km de altitude, pressão cai para ~37% (1/e ≈ 0.368)
- A 50 km: $P = 600 \cdot e^{-50/11.1} = 600 \cdot 0.011 \approx 6.6$ Pa
- Atmosfera é muito fina; retrofoguetes menos efetivos em altitudes altas

**Aplicação ao MGPEB:**
Critério de ativação de paraquedas:
- Paraquedas efetivo apenas abaixo de ~30 km (mínimo ~10 Pa dinâmico)
- Maior parte da desaceleração vem de retrofoguetes (diferente de Apolo/Artemis na Lua)

---

## PÁGINA 6-7: CONTEXTUALIZAÇÃO HISTÓRICA

### Evolução da Computação

**ENIAC (1946):**
- 30 toneladas, 30 m³, consome 150 kW
- ~5.000 operações/segundo
- Demonstrou viabilidade de computadores de propósito geral

**Histórico relevante ao MGPEB:**
1. **Computadores de Propósito Geral** → Sistemas Embarcados (1970s-80s)
   - Processadores especializados para aplicações críticas
   - Confiabilidade > Velocidade

2. **Sistemas Críticos em Aviação/Espaço**
   - Apollo Guidance Computer (1967): 64 KB RAM, mas suficiente para Lua
   - SpaceX Falcon 9: Computador autônomo com tolerância falhas (triple redundancy)

3. **Hardware em Marte (Perseverance, Curiosity)**
   - CPU: ~1 GHz (Terra: ~3+ GHz)
   - RAM: 256 MB (Terra: ~8+ GB)
   - Armazenamento: ~500 MB SSD (Terra: ~512 GB)
   - **Razão**: Proteção contra radiação cósmica (chips mais lentos = menos dano)

### Limitações do MGPEB em Marte

**Computação:**
- Memory-constrained: Estruturas lineares em vez de árvores
- CPU-constrained: Algoritmos O(n²) aceitáveis apenas para n < 10
- Communication-latency: 22 minutos Terra→Marte, decisões autônomas críticas

**Energia:**
- Powered by solar + nuclear battery backup
- Sistema MGPEB consome ~50W contínuo (marginal, aceitável)

**Ambiente:**
- Radiação danifica componentes: redundância necessária
- Erosão por areia marciana: manutenção requerida

### Escolhas Arquiteturais Justificadas

| Escolha | Razão | Alternativa Rejeitada |
|---------|-------|----------------------|
| Bubble Sort | O(n²) simples, n=5 | Merge Sort (mais complexo memoria) |
| Listas/Filas | Acesso sequencial | Árvores (mais overhead) |
| Busca Linear | Transparente, debugável | Hash Tables (nova dependência) |
| Funções Analíticas | Sem bibliotecas | Bibliotecas NumPy/SciPy (+50 MB) |
| Automata Booleano | Determinístico | Machine Learning (não-determinístico) |

---

## PÁGINA 8: GOVERNANÇA ESG

### Environmental (Ambiental)

**Preservação do Ambiente Marciano:**
- Escolha de pouso em área já impactada (não em sítios de interesse astrobiológico)
- O sistema prioriza Laboratório (M3) para coleta de dados → justifica sua posição 4
- Resíduos da fundação geridos: combustível não queimado é reciclável

**Gestão de Energia:**
- Modelagem matemática de ciclo solar permite otimizar geração
- Backup nuclear reduz dependência de painéis (resiliência)

### Social (Aspecto Humano)

**Priorização Ética:**
- M5 (Médico) = Prioridade 1, mesmo com combustível crítico
- Decisão explícita: vida humana > recursos
- Não arbitrária: critério documentado no cabeçalho

**Transparência Operacional:**
- Histórico de alertas em pilha LIFO: auditável
- Cada decisão logada: quem determinou, quando, por quê
- Código-fonte aberto para revisão

**Responsabilidade:**
- Limite de segurança `iteracoes < 10` previne loops infinitos
- Estatísticas precisas registram erros e emergências

### Governance (Político-Corporativo)

**Decisões Verificáveis:**
- Algoritmo de Bubble Sort: determinístico, reproduzível
- Portas lógicas: regras públicas, não-discriminatórias
- Dados de entrada conhecidos: cada módulo tem atributos completos

**Auditoria Contínua:**
- Relatório final consolida: tentativas, sucessos, negações, emergências
- Sistema pronto para integração com Human Oversight Loop
  (astronautas terão 22 min para revisar antes de ativação final)

**Não-Arbitrariedade:**
```python
if pouso_padrao:
    return "AUTORIZADO (Padrão)"
elif emergencia_autorizada:
    # Log automático
    return "AUTORIZADO (Emergência)"
else:
    return "NEGADO (Abortar aproximação)"
```
Cada branch tem justificativa lógica clara.

---

## PÁGINA 9: Exemplo de Execução

Incluir saída completa do programa:
```
================================================================================
MGPEB: Sistema de Gerenciamento de Pouso - AURORA SIGER
================================================================================

[1] Fila de pouso ORDENADA por prioridade:
  [M5] Médico       | Prioridade: 1 | Combustível:  10% | Criticidade: alta
  [M2] Energia      | Prioridade: 2 | Combustível:  60% | Criticidade: alta
  ...

[Relatório Final] 
  Módulos Pousados: ['M5']
  Aguardando: [M1, M3, M4, M2]
  Emergências: 1
```

---

## PÁGINA 10: CONCLUSÃO

**Resumo:**

O MGPEB demonstra integração harmoniosa entre:
✅ Estruturas de dados clássicas (fila, pilha, lista)  
✅ Algoritmos eficientes para hardware restrito  
✅ Modelagem matemática de fenômenos físicos reais  
✅ Decisões éticas baseadas em lógica formal (portas lógicas)  
✅ Governança transparente e auditável (ESG)  
✅ Documentação histórica contextualizada (evolução computação)  

**Próximas Fases Sugeridas:**
1. Integração com sistema de telemetria em tempo real
2. Simulador de dinâmica orbital (propagador de trajetória)
3. Hardware-in-the-loop: testes com computador real de Marte
4. Multi-módulo simultâneo: scheduler for múltiplos pousos
5. Falha-tolerância: redundância em sensores críticos

---

**Fim do Relatório**
