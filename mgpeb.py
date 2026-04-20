# Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)
# Integrantes: [Maria Eduarda Fernandes de Oliveira]

# 1. Cadastro de Módulos (Representados como dicionários)
from py_compile import main


modulos = [
    {"id": "M1", "tipo": "Habitação", "prioridade": 3, "combustivel_pct": 80},
    {"id": "M2", "tipo": "Energia", "prioridade": 2, "combustivel_pct": 60},
    {"id": "M3", "tipo": "Laboratório", "prioridade": 4, "combustivel_pct": 90},
    {"id": "M4", "tipo": "Logística", "prioridade": 5, "combustivel_pct": 70},
    {"id": "M5", "tipo": "Médico", "prioridade": 1, "combustivel_pct": 10} # Combustível crítico
]

# Estruturas Lineares
fila_pouso = []         # Queue (FIFO - controlada por append/pop(0))
lista_pousados = []     # Lista de registro
pilha_alertas = []      # Stack (LIFO - controlada por append/pop)

# Adicionando módulos na fila de pouso inicial
for mod in modulos:
    fila_pouso.append(mod)

# 2. Algoritmo de Ordenação (Bubble Sort por Prioridade - 1 é mais crítico)
def ordenar_fila_por_prioridade(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j]['prioridade'] > fila[j + 1]['prioridade']:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# 3. Algoritmo de Busca (Busca Linear por nível de combustível baixo)
def buscar_emergencia_combustivel(fila, limite=20):
    emergencias = []
    for mod in fila:
        if mod['combustivel_pct'] < limite:
            emergencias.append(mod)
    return emergencias

# 4. Avaliação de Regras Lógicas (Portas Lógicas)
def avaliar_pouso(modulo, clima_ok, area_livre, sensores_ok):
    c = modulo['combustivel_pct'] >= 20
    a = clima_ok
    l = area_livre
    s = sensores_ok
    
    # Expressão Booleana baseada no projeto
    pouso_padrao = c and a and l and s
    emergencia_autorizada = (not c) and l and s
    
    if pouso_padrao:
        return "AUTORIZADO (Padrão)"
    elif emergencia_autorizada:
        pilha_alertas.append(f"ALERTA: {modulo['id']} pouso forçado por falta de combustível!")
        return "AUTORIZADO (Emergência)"
    else:
        return "NEGADO (Abortar aproximação)"

# --- EXECUÇÃO DO PROTÓTIPO ---

print("=== MGPEB: Sistema Inicializado ===")

# Ordenando a fila baseada na criticidade
fila_pouso = ordenar_fila_por_prioridade(fila_pouso)
print("\nFila de pouso ordenada por prioridade:")
for m in fila_pouso:
    print(f"[{m['id']}] {m['tipo']} - Prioridade: {m['prioridade']} - Combustível: {m['combustivel_pct']}%")

print("\n--- Iniciando Simulação de Pouso ---")
# Simulação de variáveis da atmosfera/base no momento atual
clima_atual_ok = False # Tempestade de areia simulada
area_pouso_livre = True
sensores_navegacao_ok = True

while len(fila_pouso) > 0:
    # Retira o primeiro da fila (FIFO)
    modulo_atual = fila_pouso.pop(0)
    print(f"\nAvaliação do Módulo: {modulo_atual['id']} ({modulo_atual['tipo']})")
    
    decisao = avaliar_pouso(modulo_atual, clima_atual_ok, area_pouso_livre, sensores_navegacao_ok)
    print(f"Decisão do Sistema: {decisao}")
    
    if "AUTORIZADO" in decisao:
        lista_pousados.append(modulo_atual)
    else:
        print(f"{modulo_atual['id']} enviado para o final da fila orbital.")
        fila_pouso.append(modulo_atual) # Volta para o fim da fila
        break # Interrompe a simulação por segurança climática

print("\n--- Relatório Final ---")
print(f"Módulos Pousados com Sucesso: {[m['id'] for m in lista_pousados]}")
print(f"Alertas Críticos Registrados na Pilha: {len(pilha_alertas)}")
while pilha_alertas:
    print(pilha_alertas.pop()) # Esvaziando a pilha de alertas (LIFO)
