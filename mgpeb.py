# ===============================================================================
# Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
# Missão Aurora Siger - Colônia em Marte
# ===============================================================================
# Integrantes: [Maria Eduarda Fernandes de Oliveira]
#
# CONTEXTUALIZAÇÃO - EVOLUÇÃO DA COMPUTAÇÃO E LIMITAÇÕES EM MARTE:
# Este sistema reflete a importância de algoritmos eficientes e estruturas de
# dados otimizadas. Assim como os primeiros computadores de propósito geral
# (ENIAC, 1946) abriram caminho para sistemas embarcados críticos, o MGPEB
# deve funcionar com restrições severas em Marte:
#   - Memória limitada: ~256 MB para os sistemas de bordo
#   - Processamento: ~1 GHz (inferior aos padrões terrestres atuais)
#   - Consumo energético crítico: alimentado por painéis solares + baterias
#   - Tolerância à radiação: estrutura computacional endurecida
#
# Essas limitações justificam a escolha de:
#   - Bubble Sort em vez de algoritmos mais complexos (menor uso de memória)
#   - Estruturas lineares (listas, filas, pilhas) em vez de árvores avançadas
#   - Validações booleanas simples mas robustas (portas lógicas)
#
# PRINCÍPIOS ESG - GOVERNANÇA NA BASE AURORA SIGER:
# A colônia opera sob perspectiva de sustentabilidade:
#   ENVIRONMENTAL: Minimização de impacto, gestão de resíduos, energia limpa
#   SOCIAL: Segurança, transparência, responsabilidade
#   GOVERNANCE: Decisões verificáveis, não arbitrárias, auditoria contínua
#
# ===============================================================================

import math

# ===============================================================================
# 1. CADASTRO DE MÓDULOS
# ===============================================================================

modulos = [
    {"id": "M1", "tipo": "Habitação", "prioridade": 3, "combustivel_pct": 80},
    {"id": "M2", "tipo": "Energia", "prioridade": 2, "combustivel_pct": 60},
    {"id": "M3", "tipo": "Laboratório", "prioridade": 4, "combustivel_pct": 90},
    {"id": "M4", "tipo": "Logística", "prioridade": 5, "combustivel_pct": 70},
    {"id": "M5", "tipo": "Médico", "prioridade": 1, "combustivel_pct": 10}
]

# ===============================================================================
# 2. ESTRUTURAS LINEARES
# ===============================================================================

fila_pouso = []           # Queue (FIFO) - módulos aguardando pouso
lista_pousados = []       # Lista de módulos pousados com sucesso
pilha_alertas = []        # Stack (LIFO) - histórico de alertas

# Preenchendo a fila inicial
for mod in modulos:
    fila_pouso.append(mod)

# ===============================================================================
# 3. FUNÇÃO MATEMÁTICA - MODELAGEM DE ALTURA EM DESCIDA
# ===============================================================================

def calcular_altura_descida(h0_km, v0_kmps, tempo_seg):
    """
    Calcula a altura do módulo durante descida em Marte
    
    Modelo Quadrático: h(t) = h₀ - v₀·t - (1/2)·g·t²
    
    Parâmetros:
      h0_km: altura inicial em quilômetros
      v0_kmps: velocidade inicial de descida em km/s
      tempo_seg: tempo decorrido em segundos
      
    Significado físico:
      - A altura diminui linearmente com a velocidade (v₀·t)
      - A altura diminui ainda mais com a aceleração gravitacional ((1/2)·g·t²)
      - Ao ajustar retrofoguetes, reduz-se v₀ para pousar com segurança
      
    Constante de Marte:
      g = 3.71 m/s² = 0.003711 km/s²
    """
    g_marte = 0.003711  # km/s²
    altura = h0_km - (v0_kmps * tempo_seg) - (0.5 * g_marte * tempo_seg**2)
    return max(0, altura)

# ===============================================================================
# 4. ALGORITMO DE ORDENAÇÃO - BUBBLE SORT
# ===============================================================================

def ordenar_fila_por_prioridade(fila):
    """
    Ordena a fila de pouso por prioridade usando Bubble Sort
    Complexidade: O(n²), mas aceitável para n=5 em sistemas embarcados
    Prioridade 1 = mais crítico (deve pousar primeiro)
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j]['prioridade'] > fila[j + 1]['prioridade']:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# ===============================================================================
# 5. ALGORITMOS DE BUSCA
# ===============================================================================

def buscar_emergencia_combustivel(fila, limite=20):
    """
    Busca Linear: Identifica módulos com combustível crítico (< limite%)
    Complexidade: O(n)
    """
    emergencias = []
    for mod in fila:
        if mod['combustivel_pct'] < limite:
            emergencias.append(mod)
    return emergencias

def buscar_modulos_por_tipo(tipo_buscado, modulos_lista):
    """
    Busca Linear: Filtra módulos por tipo específico
    Complexidade: O(n)
    """
    resultado = []
    for mod in modulos_lista:
        if mod['tipo'] == tipo_buscado:
            resultado.append(mod)
    return resultado

# ===============================================================================
# 6. AVALIAÇÃO DE REGRAS LÓGICAS - PORTAS LÓGICAS
# ===============================================================================

def avaliar_pouso(modulo, clima_ok, area_livre, sensores_ok):
    """
    Avalia autorização de pouso usando portas lógicas (AND, OR, NOT)
    
    Variáveis booleanas:
      c = combustível ≥ 20%
      a = clima adequado
      l = área de pouso livre
      s = sensores de navegação ok
      
    Expressões:
      Pouso Padrão = c AND a AND l AND s
      Pouso Emergência = (NOT c) AND l AND s
      Pouso Negado = negação das anteriores
    """
    c = modulo['combustivel_pct'] >= 20
    a = clima_ok
    l = area_livre
    s = sensores_ok
    
    # Portas lógicas compostas
    pouso_padrao = c and a and l and s
    emergencia_autorizada = (not c) and l and s
    
    if pouso_padrao:
        return "AUTORIZADO (Padrão)"
    elif emergencia_autorizada:
        pilha_alertas.append(f"ALERTA: {modulo['id']} pouso forçado por falta de combustível!")
        return "AUTORIZADO (Emergência)"
    else:
        return "NEGADO (Abortar aproximação)"

# ===============================================================================
# 7. EXECUÇÃO DO PROTÓTIPO - SIMULAÇÃO
# ===============================================================================

print("\n" + "=" * 80)
print("MGPEB: Sistema de Gerenciamento de Pouso - AURORA SIGER")
print("=" * 80)

# Ordenação da fila
fila_pouso = ordenar_fila_por_prioridade(fila_pouso)
print("\n[PASSO 1] Fila de pouso ORDENADA por prioridade (Bubble Sort):")
print("-" * 80)
for m in fila_pouso:
    print(f"  [{m['id']}] {m['tipo']:15} - Prioridade: {m['prioridade']} - " +
          f"Combustível: {m['combustivel_pct']:3}%")

# Busca de emergências
print("\n[PASSO 2] Análise de emergências (Busca Linear):")
print("-" * 80)
emergencias = buscar_emergencia_combustivel(fila_pouso, limite=20)
if emergencias:
    print(f"  Encontrados {len(emergencias)} módulo(s) com combustível crítico:")
    for e in emergencias:
        print(f"    - [{e['id']}] {e['tipo']} com {e['combustivel_pct']}%")
else:
    print("  Nenhum módulo em situação crítica.")

# Busca por tipo
print("\n[PASSO 3] Busca de módulos por tipo (Busca Linear):")
print("-" * 80)
tipo_busca = "Médico"
resultado_busca = buscar_modulos_por_tipo(tipo_busca, modulos)
print(f"  Módulos do tipo '{tipo_busca}': {[m['id'] for m in resultado_busca]}")

# Simulação de pouso com condições
print("\n[PASSO 4] Simulação de pouso com Portas Lógicas:")
print("-" * 80)
clima_atual_ok = False      # Tempestade de areia
area_pouso_livre = True
sensores_navegacao_ok = True

print(f"  Condições: Clima={clima_atual_ok}, Área livre={area_pouso_livre}, " +
      f"Sensores={sensores_navegacao_ok}")
print("  Processando fila:\n")

iteracoes = 0  # Trava de segurança: previne loop infinito
while len(fila_pouso) > 0 and iteracoes < 10:
    modulo_atual = fila_pouso.pop(0)
    iteracoes += 1
    
    print(f"  [{iteracoes}] Módulo {modulo_atual['id']} ({modulo_atual['tipo']})")
    
    decisao = avaliar_pouso(
        modulo_atual, clima_atual_ok, area_pouso_livre, sensores_navegacao_ok
    )
    print(f"      Decisão: {decisao}")
    
    if "AUTORIZADO" in decisao:
        lista_pousados.append(modulo_atual)
        print(f"      ✓ Pouso registrado com sucesso.")
    else:
        fila_pouso.append(modulo_atual)  # Volta para o fim
        print(f"      ✗ Retornado à fila orbital.")
        break  # Interrompe por segurança climática

# ===============================================================================
# 8. RELATÓRIO FINAL
# ===============================================================================

print("\n" + "=" * 80)
print("RELATÓRIO FINAL - ESTATÍSTICAS DE OPERAÇÃO")
print("=" * 80)

print(f"\nMódulos Pousados com Sucesso: {[m['id'] for m in lista_pousados]}")
print(f"Total: {len(lista_pousados)}")

print(f"\nMódulos Aguardando em Órbita: {[m['id'] for m in fila_pouso]}")
print(f"Total: {len(fila_pouso)}")

print(f"\nAlertas Críticos Registrados (Pilha - LIFO):")
if pilha_alertas:
    while pilha_alertas:
        print(f"  ⚠ {pilha_alertas.pop()}")
else:
    print("  Nenhum alerta.")

# ===============================================================================
# 9. DEMONSTRAÇÃO DA FUNÇÃO MATEMÁTICA
# ===============================================================================

print("\n" + "=" * 80)
print("DEMONSTRAÇÃO - FUNÇÃO MATEMÁTICA: Altura em Descida")
print("=" * 80)
print("\nModelo: h(t) = h₀ - v₀·t - (1/2)·g·t²")
print("Parâmetros: h₀ = 50 km, v₀ = 0.5 km/s, g = 0.003711 km/s² (Marte)\n")

print("Evolução da altura ao longo do tempo:")
for t in [0, 50, 100, 150, 200]:
    h = calcular_altura_descida(50, 0.5, t)
    print(f"  t = {t:3}s → h(t) = {h:7.2f} km")

print("\n" + "=" * 80)
print("Fim da simulação MGPEB")
print("=" * 80 + "\n")
