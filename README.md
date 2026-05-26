# Sistema de Modelagem de Moléculas e Ligações Químicas

## Descrição Geral

Este é um sistema de **Programação Orientada a Objetos** (POO) que modela elementos químicos, átomos individuais e ligações covalentes, permitindo a representação e análise de moléculas químicas.

## Estrutura do Projeto

```
POO/
├── elemento.py      # Define a classe Elemento
├── atomo.py         # Define a classe Atomo
├── ligacao.py       # Define a classe Ligacao
├── molecula.py      # Define a classe Molecula
├── main.py          # Script de demonstração
└── README.md        # Este arquivo
```

## Classes Principais

### 1. **Classe `Elemento`** (elemento.py)

Representa um elemento químico da tabela periódica.

**Características principais:**
- **Imutável**: Uma vez criado, não pode ser modificado
- **Hashable**: Pode ser usado como chave de dicionário
- Validação rigorosa de todos os parâmetros

**Atributos:**
- `simbolo` (str): Símbolo do elemento (ex: "H", "O", "C")
- `nome` (str): Nome do elemento (ex: "Hidrogênio")
- `numero_atomico` (int): Número de prótons
- `massa_atomica` (float): Massa em unidades atômicas
- `valencia_maxima` (int): Número máximo de ligações covalentes (1-8)

**Métodos importantes:**
- `__str__()`: Representação legível (ex: "H (Hidrogênio): Z=1, massa=1.008 u")
- `__hash__()`: Permite usar como chave em dicionários
- `__eq__()`: Compara elementos pelo símbolo
- Getters (@property) para acesso aos atributos

### 2. **Classe `Atomo`** (atomo.py)

Representa um átomo individual dentro de uma molécula.

**Características principais:**
- **IDs únicos automáticos**: Cada átomo recebe um ID sequencial
- **Contador de classe**: Mantém controle global de todos os IDs

**Atributos:**
- `elemento` (Elemento): Referência ao elemento químico
- `id` (int): Identificador único gerado automaticamente

**Métodos importantes:**
- `__init__(elemento)`: Cria um novo átomo com ID único
- `__str__()`: Representação (ex: "H#1", "C#5")
- Getters para elemento e id (somente leitura)

**Exemplo:**
```python
H = Elemento("H", "Hidrogênio", 1, 1.008, 1)
atomo1 = Atomo(H)  # Recebe id=1
atomo2 = Atomo(H)  # Recebe id=2
```

### 3. **Classe `Ligacao`** (ligacao.py)

Representa uma ligação covalente entre dois átomos.

**Características principais:**
- Suporta 3 tipos de ligação: simples (1), dupla (2) e tripla (3)
- Validação de integridade: os átomos devem ser diferentes

**Atributos:**
- `atomo1` (Atomo): Primeiro átomo
- `atomo2` (Atomo): Segundo átomo
- `ordem` (int): Tipo de ligação (1, 2 ou 3)

**Métodos importantes:**
- `__init__(atomo1, atomo2, ordem=1)`: Cria ligação com validação
- `get_outro_atomo(atomo)`: Dado um átomo, retorna seu vizinho
- `__str__()`: Representação (ex: "H#1 - O#3 (simples)", "C#3 ≡ C#4 (tripla)")

### 4. **Classe `Molecula`** (molecula.py)

Gerencia uma coleção de átomos e ligações que formam uma molécula.

**Características principais:**
- **Composição automática**: Calculada sempre que necessário a partir dos átomos
- **Ligações validadas**: Evita duplicatas e garante integridade
- Cálculos de propriedades moleculares

**Atributos:**
- `nome` (str): Nome da molécula
- `atomos` (list): Lista de átomos
- `ligacoes` (list): Lista de ligações

**Métodos importantes:**

| Método | Descrição |
|--------|-----------|
| `adicionar_elemento(elemento, quantidade)` | Cria e adiciona novos átomos |
| `remover_atomo(atomo)` | Remove um átomo e suas ligações |
| `adicionar_ligacao(atomo1, atomo2, ordem)` | Cria ligação entre dois átomos |
| `calcular_composicao()` | Retorna dicionário {Elemento: quantidade} |
| `calcular_massa_molecular()` | Calcula massa total em u |
| `exibir_formula()` | Gera fórmula molecular (ex: "H2O") |
| `obter_vizinhos(atomo)` | Lista átomos conectados com ordens |
| `obter_grau(atomo)` | Soma das ordens das ligações |
| `validar_valencia()` | Verifica se respeita valência máxima |

## Como Executar

### Pré-requisitos
- Python 3.7+

### Executar o programa
```bash
cd POO
python main.py
```

## Exemplo de Uso

```python
from elemento import Elemento
from molecula import Molecula

# Cria elementos
H = Elemento("H", "Hidrogênio", 1, 1.008, 1)
O = Elemento("O", "Oxigênio", 8, 16.00, 2)

# Cria molécula de água
agua = Molecula("Água")
agua.adicionar_elemento(H, 2)
agua.adicionar_elemento(O, 1)

# Recupera átomos
h_atoms = [a for a in agua.atomos if a.elemento == H]
o_atom = [a for a in agua.atomos if a.elemento == O][0]

# Adiciona ligações
agua.adicionar_ligacao(h_atoms[0], o_atom, 1)
agua.adicionar_ligacao(h_atoms[1], o_atom, 1)

# Exibe informações
print(agua)
print(f"Fórmula: {agua.exibir_formula()}")
print(f"Massa: {agua.calcular_massa_molecular():.3f} u")
print(f"Válida? {agua.validar_valencia()}")
```

## Conceitos Implementados

### Validação e Encapsulamento
- Validação de tipos em todos os __init__
- Uso de @property para acesso controlado (somente leitura)
- Atributos privados com prefixo `_`

### Composição
- Elemento → Atomo (cada átomo é de um elemento específico)
- Atomo + Atomo → Ligacao
- Atom + Ligacao → Molecula

### Associações
- Molecula contém múltiplos Atomos
- Molecula contém múltiplas Ligacoes
- Ligacao conecta dois Atomos diferentes

### Geração Automática de IDs
- Classe Atomo usa contador de classe (_proximo_id)
- Cada instância incrementa o contador
- IDs são sequenciais globalmente

### Validação de Regras Químicas
- Valência máxima respeita número máximo de ligações
- Método `validar_valencia()` verifica integridade
- Cálculo de grau (valência aparente) através de `obter_grau()`

## Moléculas Demonstradas

1. **Água (H2O)**: Molécula simples com 3 átomos e 2 ligações
2. **Metano (CH4)**: Hidrocarboneto com 5 átomos e 4 ligações
3. **Etanol (C2H6O)**: Álcool com 9 átomos e 8 ligações

Todas as moléculas demonstradas passam na validação de valência.
