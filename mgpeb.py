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
#   - Latência de comunicação: ~22 minutos (distância Terra-Marte)
#
# Essas limitações justificam a escolha de:
#   - Bubble Sort em vez de algoritmos mais complexos (menor uso de memória)
#   - Estruturas lineares (listas, filas, pilhas) em vez de árvores avançadas
#   - Funções matemáticas analíticas diretas (sem bibliotecas pesadas)
#   - Validações booleanas simples mas robustas (portas lógicas)
#
# PRINCÍPIOS ESG - GOVERNANÇA NA BASE AURORA SIGER:
# A colônia deverá operar sob perspectiva de sustentabilidade:
#   ENVIRONMENTAL: Minimização de impacto, gestão de resíduos, energia limpa
#   SOCIAL: Segurança, transparência, responsabilidade
#   GOVERNANCE: Decisões verificáveis, não arbitrárias, con auditoria contínua
#
# ===============================================================================

import math

# ===============================================================================
# 1. CADASTRO DE MÓDULOS COM ATRIBUTOS COMPLETOS
# ===============================================================================
# Cada módulo representa um componente crítico da colônia Aurora Siger
# Atributos:
#   - id: identificador único (M1-M5)
#   - tipo: função no cenário (Habitação, Energia, Laboratório, Logística, Médico)
#   - prioridade: (1=crítica, 5=suporte) - determina ordem de pouso
#   - combustivel_pct: percentual de combustível restante (0-100%)
#   - massa_kg: massa do módulo em quilogramas
#   - criticidade_carga: nível de risco da carga (baixa, média, alta)
#   - eta_minutos: tempo estimado de chegada à órbita (minutos)

modulos = [
    {
        "id": "M1", "tipo": "Habitação", "prioridade": 3, "combustivel_pct": 80,
        "massa_kg": 4500, "criticidade_carga": "média", "eta_minutos": 25
    },
    {
        "id": "M2", "tipo": "Energia", "prioridade": 2, "combustivel_pct": 60,
        "massa_kg": 3200, "criticidade_carga": "alta", "eta_minutos": 18
    },
    {
        "id": "M3", "tipo": "Laboratório", "prioridade": 4, "combustivel_pct": 90,
        "massa_kg": 2800, "criticidade_carga": "média", "eta_minutos": 32
    },
    {
        "id": "M4", "tipo": "Logística", "prioridade": 5, "combustivel_pct": 70,
        "massa_kg": 5100, "criticidade_carga": "baixa", "eta_minutos": 40
    },
    {
        "id": "M5", "tipo": "Médico", "prioridade": 1, "combustivel_pct": 10,
        "massa_kg": 2200, "criticidade_carga": "alta", "eta_minutos": 15
    }
]


# ===============================================================================
# 2. ESTRUTURAS LINEARES - ORGANIZAÇÃO DE DADOS
# ===============================================================================
# Fila (Queue - FIFO): Módulos aguardando autorização de pouso
fila_pouso = []

# Lista: Módulos já pousados com sucesso
lista_pousados = []

# Lista auxiliar: Módulos em condição de alerta (combustível crítico, etc.)
lista_alertas_criticos = []

# Pilha (Stack - LIFO): Histórico de alertas para visualização em ordem reversa
pilha_alertas = []

# Dicionário: Rastreamento de módulos por tipo (suporte a buscas rápidas)
modulos_por_tipo = {}

# Dicionário: Estatísticas de operação
estatisticas_pouso = {
    "total_tentativas": 0,
    "sucessos": 0,
    "negacoes": 0,
    "emergencias": 0,
    "consumo_combustivel_total": 0.0
}

# Preenchendo a fila de pouso inicial
for mod in modulos:
    fila_pouso.append(mod)
    tipo = mod["tipo"]
    if tipo not in modulos_por_tipo:
        modulos_por_tipo[tipo] = []
    modulos_por_tipo[tipo].append(mod["id"])


# ===============================================================================
# 3. FUNÇÕES MATEMÁTICAS APLICADAS AO POUSO E ESTABILIZAÇÃO
# ===============================================================================

# FUNÇÃO 1: Altura em função do tempo de descida (função quadrática)
# Modelo: h(t) = h₀ - v₀*t - (1/2)*g*t²
# Onde:
#   - h₀ = altura inicial (em km)
#   - v₀ = velocidade inicial de descida (km/s)
#   - g = aceleração gravitacional em Marte ≈ 3.71 m/s² = 0.003711 km/s²
#   - t = tempo (em segundos)
# Significado: quanto mais tempo passa, menor é a altura do módulo
# Uma retrofoguetagem adequada deve reduzir v₀ para manter h(t) > 0 até o solo

def calcular_altura_descida(h0_km, v0_kmps, tempo_seg):
    """
    Calcula a altura do módulo durante descida em Marte
    h(t) = h₀ - v₀*t - (1/2)*g*t²
    """
    g_marte = 0.003711  # km/s²
    altura = h0_km - (v0_kmps * tempo_seg) - (0.5 * g_marte * tempo_seg**2)
    return max(0, altura)  # Garante que altura não seja negativa

# FUNÇÃO 2: Temperatura externa vs tempo (função exponencial decrescente)
# Modelo: T(t) = T_noite + (T_dia - T_noite) * e^(-t/τ)
# Onde:
#   - T_dia ≈ 250 K (durante o dia em Marte)
#   - T_noite ≈ 130 K (durante a noite)
#   - τ = constante de tempo (horas)
#   - t = tempo (horas)
# Significado: temperatura oscila entre noite e dia; afeta painéis solares e
#   sistemas de aquecimento. Pousos durante o dia são preferíveis.

def calcular_temperatura_ambiente(horas_desde_amanhecer):
    """
    Simula temperatura ambiente em Marte ao longo de 24 horas marcianas
    Ciclo: -123°C (noite) até -23°C (dia)
    """
    T_dia_kelvin = 250
    T_noite_kelvin = 130
    tau_horas = 6  # Constante de tempo (~6 horas)
    
    # Temperatura aproximada como função cosseno (mais realista que exponencial)
    t_normalizado = (horas_desde_amanhecer % 24.65) / 24.65  # Dia marciano = 24.65h
    temp_kelvin = T_noite_kelvin + (T_dia_kelvin - T_noite_kelvin) * (0.5 + 0.5 * math.cos(2 * math.pi * t_normalizado))
    temp_celsius = temp_kelvin - 273.15
    return temp_celsius

# FUNÇÃO 3: Consumo de combustível em função da velocidade (função quadrática)
# Modelo: F(v) = a*v² + b*v + c
# Onde:
#   - v = velocidade de descida em m/s
#   - a, b, c = coeficientes do modelo (tuning necessário)
# Significado: quanto maior a velocidade, maior o consumo de combustível para
#   retrofoguetagem. Há um trade-off entre segurança (descida lenta) e
#   eficiência (descida rápida).

def calcular_consumo_combustivel(velocidade_mps, tempo_retrofoguetes_seg):
    """
    Estima consumo de combustível baseado em veloc. e tempo de retrofoguetes
    Modelo simplificado: consumo = 0.05 * v² + 2.0 * t
    (coeficientes ajustados para Marte)
    """
    consumo_por_velocidade = 0.05 * (velocidade_mps ** 2)
    consumo_por_tempo = 2.0 * tempo_retrofoguetes_seg
    consumo_total_pct = (consumo_por_velocidade + consumo_por_tempo)
    return min(100, consumo_total_pct)  # Cap at 100%

# FUNÇÃO 4: Geração de energia solar ao longo do dia (função cosseno)
# Modelo: E(t) = E_max * cos²(π*t / T)
# Onde:
#   - E_max = potência máxima dos painéis (kW)
#   - t = tempo (horas)
#   - T = período (24.65 horas em Marte)
# Significado: energia solar varia com posição do Sol. Afeta carregamento de
#   baterias e consumo de energia. Decisões de pouso devem considerar ciclo
#   de energia disponível.

def calcular_geracao_energia_solar(horas_desde_amanhecer, potencia_max_kw=5.0):
    """
    Simula geração de energia solar ao longo do dia marciano
    Retorna potência em kW
    """
    t_normalizado = (horas_desde_amanhecer % 24.65) / 24.65
    potencia = potencia_max_kw * (math.cos(math.pi * t_normalizado) ** 2)
    return max(0, potencia)  # Sem energia à noite

# FUNÇÃO 5: Pressão atmosférica em função da altitude (função exponencial)
# Modelo: P(h) = P₀ * e^(-h/H)
# Onde:
#   - P₀ = pressão ao nível da superfície (~600 Pa em Marte)
#   - h = altitude (km)
#   - H = altura de escala (~11.1 km em Marte)
# Significado: densidade do ar decresce exponencialmente. Afeta eficiência de
#   paraquedas e dinâmica de descida.

def calcular_pressao_atmosferica(altitude_km):
    """
    Calcula pressão atmosférica em Marte em função da altitude
    P(h) = P₀ * e^(-h/H)
    """
    P0_pascais = 600
    H_escala = 11.1
    pressao = P0_pascais * math.exp(-altitude_km / H_escala)
    return pressao

# ===============================================================================
# 4. ALGORITMOS DE ORDENAÇÃO E BUSCA
# ===============================================================================

def ordenar_fila_por_prioridade(fila):
    """
    Ordena a fila de pouso por prioridade usando Bubble Sort
    Prioridade 1 = mais crítico (deve pousar primeiro)
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j]['prioridade'] > fila[j + 1]['prioridade']:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

def buscar_emergencia_combustivel(fila, limite=20):
    """
    Identifica módulos com combustível abaixo do limite crítico
    """
    emergencias = []
    for mod in fila:
        if mod['combustivel_pct'] < limite:
            emergencias.append(mod)
    return emergencias

def buscar_modulos_por_tipo(tipo_buscado):
    """
    Retorna IDs de todos os módulos de um tipo específico
    """
    return modulos_por_tipo.get(tipo_buscado, [])

def buscar_modulos_por_criticidade(fila, nivel_criticidade):
    """
    Filtra módulos por nível de criticidade da carga
    """
    resultado = []
    for mod in fila:
        if mod['criticidade_carga'] == nivel_criticidade:
            resultado.append(mod)
    return resultado

# ===============================================================================
# 5. AVALIAÇÃO DE REGRAS LÓGICAS - PORTAS LÓGICAS
# ===============================================================================

def avaliar_pouso(modulo, clima_ok, area_livre, sensores_ok):
    """
    Avalia autorização de pouso usando portas lógicas
    AND, OR, NOT para expressões booleanas compostas
    """
    c = modulo['combustivel_pct'] >= 20
    a = clima_ok
    l = area_livre
    s = sensores_ok
    
    pouso_padrao = c and a and l and s
    emergencia_autorizada = (not c) and l and s
    
    if pouso_padrao:
        return "AUTORIZADO (Padrão)"
    elif emergencia_autorizada:
        pilha_alertas.append(f"ALERTA: {modulo['id']} pouso forçado por falta de combustível!")
        estatisticas_pouso["emergencias"] += 1
        return "AUTORIZADO (Emergência)"
    else:
        return "NEGADO (Abortar aproximação)"

# ===============================================================================
# 6. EXECUÇÃO DO PROTÓTIPO - SIMULAÇÃO DE POUSO
# ===============================================================================

print("=" * 80)
print("MGPEB: Sistema de Gerenciamento de Pouso - AURORA SIGER")
print("=" * 80)

fila_pouso = ordenar_fila_por_prioridade(fila_pouso)
print("\n[1] Fila de pouso ORDENADA por prioridade:")
print("-" * 80)
for m in fila_pouso:
    print(f"  [{m['id']}] {m['tipo']:12} | Prioridade: {m['prioridade']} | "
          f"Combustível: {m['combustivel_pct']:3}% | Criticidade: {m['criticidade_carga']}")

print("\n[2] Análise de EMERGÊNCIAS:")
print("-" * 80)
emergencias = buscar_emergencia_combustivel(fila_pouso, limite=20)
if emergencias:
    print(f"  Encontrados {len(emergencias)} módulos com combustível crítico:")
    for e in emergencias:
        print(f"    - [{e['id']}] {e['tipo']} com {e['combustivel_pct']}% de combustível")
else:
    print("  Nenhum módulo em situação crítica de combustível.")

print("\n[3] Módulos INDEXADOS por tipo:")
print("-" * 80)
for tipo, ids in modulos_por_tipo.items():
    print(f"  {tipo:15} : {ids}")

print("\n[4] Simulação de POUSO COM CONDIÇÕES VARIÁVEIS:")
print("-" * 80)
clima_atual_ok = False
area_pouso_livre = True
sensores_navegacao_ok = True

print(f"  Condições atuais: Clima={clima_atual_ok} | Área livre={area_pouso_livre} | "
      f"Sensores={sensores_navegacao_ok}")
print(f"  Iniciando pousos...\n")

iteracoes = 0
while len(fila_pouso) > 0 and iteracoes < 10:
    modulo_atual = fila_pouso.pop(0)
    iteracoes += 1
    
    print(f"  [{iteracoes}] Avaliação: {modulo_atual['id']} ({modulo_atual['tipo']})")
    
    decisao = avaliar_pouso(
        modulo_atual, clima_atual_ok, area_pouso_livre, sensores_navegacao_ok
    )
    print(f"      Decisão: {decisao}")
    
    estatisticas_pouso["total_tentativas"] += 1
    if "AUTORIZADO" in decisao:
        lista_pousados.append(modulo_atual)
        estatisticas_pouso["sucessos"] += 1
        print(f"      Status: ✓ Pouso bem-sucedido em segurança.")
    else:
        print(f"      Status: ✗ Enviado para fila orbital novamente.")
        fila_pouso.append(modulo_atual)
        estatisticas_pouso["negacoes"] += 1
        break

# ===============================================================================
# 7. RELATÓRIO FINAL
# ===============================================================================

print("\n" + "=" * 80)
print("RELATÓRIO FINAL - ESTATÍSTICAS DE OPERAÇÃO")
print("=" * 80)

print(f"\nMódulos Pousados com Sucesso ({estatisticas_pouso['sucessos']}):")
for m in lista_pousados:
    print(f"  ✓ [{m['id']}] {m['tipo']:15} - "
          f"Prioridade {m['prioridade']} - Combustível: {m['combustivel_pct']}%")

print(f"\nMódulos Aguardando em Órbita ({len(fila_pouso)}):")
for m in fila_pouso:
    print(f"  ⊙ [{m['id']}] {m['tipo']:15} - ETA: {m['eta_minutos']} min")

print(f"\n\nEstatísticas Consolidadas:")
print(f"  Total de tentativas: {estatisticas_pouso['total_tentativas']}")
print(f"  Sucessos: {estatisticas_pouso['sucessos']}")
print(f"  Negações: {estatisticas_pouso['negacoes']}")
print(f"  Pousos em emergência: {estatisticas_pouso['emergencias']}")

print(f"\n\nAlertas Críticos Registrados ({len(pilha_alertas)}):")
if pilha_alertas:
    while pilha_alertas:
        alerta = pilha_alertas.pop()
        print(f"  ⚠ {alerta}")
else:
    print("  Nenhum alerta registrado durante operação.")

print("\n" + "=" * 80)
print("DEMONSTRAÇÃO DE FUNÇÕES MATEMÁTICAS:")
print("=" * 80)

print("\n[Função 1] Altura em função do tempo de descida:")
print("  Modelo: h(t) = h₀ - v₀*t - (1/2)*g*t²")
for t in [0, 50, 100, 150, 200]:
    h = calcular_altura_descida(50, 0.5, t)
    print(f"  t = {t:3}s → h = {h:7.2f} km")

print("\n[Função 2] Temperatura ambiente ao longo do dia marciano:")
for hora in [0, 6, 12, 18, 24]:
    T = calcular_temperatura_ambiente(hora)
    print(f"  Hora = {hora:2} → T = {T:7.2f}°C")

print("\n[Função 3] Consumo de combustível por velocidade:")
for v_mps in [5, 10, 15, 20]:
    consumo = calcular_consumo_combustivel(v_mps, 100)
    print(f"  v = {v_mps:2} m/s → consumo = {consumo:6.2f}%")

print("\n[Função 4] Geração de energia solar ao longo do dia:")
for hora in [0, 6, 12, 18, 24]:
    energia = calcular_geracao_energia_solar(hora)
    print(f"  Hora = {hora:2} → Potência = {energia:5.2f} kW")

print("\n[Função 5] Pressão atmosférica em função da altitude:")
for altitude in [0, 10, 20, 30, 50]:
    pressao = calcular_pressao_atmosferica(altitude)
    print(f"  h = {altitude:2} km → P = {pressao:8.2f} Pa")

print("\n" + "=" * 80)
print("Fim da simulação MGPEB")
print("=" * 80)
