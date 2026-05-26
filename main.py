"""
Script de Demonstração - Modelagem de Moléculas e Ligações Químicas
Demonstra o uso das classes Elemento, Atomo, Ligacao e Molecula
"""

from elemento import Elemento
from atomo import Atomo
from molecula import Molecula


def main():
    """Função principal que demonstra o sistema de moléculas."""
    
    print("=" * 70)
    print("SISTEMA DE MODELAGEM DE MOLÉCULAS E LIGAÇÕES QUÍMICAS")
    print("=" * 70)
    print()
    
    # =========================================================================
    # PARTE 1: Criação de Elementos Químicos
    # =========================================================================
    print("1. CRIANDO ELEMENTOS QUÍMICOS")
    print("-" * 70)
    
    # Cria elementos com suas propriedades: símbolo, nome, número atômico,
    # massa atômica e valência máxima
    H = Elemento("H", "Hidrogênio", 1, 1.008, 1)
    O = Elemento("O", "Oxigênio", 8, 16.00, 2)
    C = Elemento("C", "Carbono", 6, 12.011, 4)
    
    print(f"Hidrogênio: {H}")
    print(f"Oxigênio:   {O}")
    print(f"Carbono:    {C}")
    print()
    
    # =========================================================================
    # PARTE 2: Molécula de Água (H2O)
    # =========================================================================
    print("2. MOLÉCUL DE ÁGUA (H2O)")
    print("-" * 70)
    
    # Cria uma molécula vazia
    agua = Molecula("Água")
    
    # Adiciona elementos: o método adicionar_elemento cria novos átomos
    # com IDs únicos gerados automaticamente
    agua.adicionar_elemento(H, 2)  # Adiciona 2 átomos de Hidrogênio (ids: 1, 2)
    agua.adicionar_elemento(O, 1)  # Adiciona 1 átomo de Oxigênio (id: 3)
    
    print(f"Átomos na molécula: {[str(a) for a in agua.atomos]}")
    print()
    
    # Recupera os átomos de forma filtragem
    atomos_H = [a for a in agua.atomos if a.elemento == H]
    oxigenio = [a for a in agua.atomos if a.elemento == O][0]
    
    print(f"Hidrogênios encontrados: {[str(h) for h in atomos_H]}")
    print(f"Oxigênio encontrado:     {oxigenio}")
    print()
    
    # Adiciona ligações entre os átomos
    # Cada ligação conecta dois átomos específicos
    agua.adicionar_ligacao(atomos_H[0], oxigenio, 1)  # Ligação simples
    agua.adicionar_ligacao(atomos_H[1], oxigenio, 1)  # Ligação simples
    
    print(f"Ligações adicionadas:")
    for lig in agua.ligacoes:
        print(f"  - {lig}")
    print()
    
    # Exibe informações calculadas da molécula
    print(f"Fórmula molecular: {agua.exibir_formula()}")
    print(f"Massa molecular:   {agua.calcular_massa_molecular():.3f} u")
    print(f"Composição:        {agua.calcular_composicao()}")
    print()
    
    # Valida a regra de valência
    valencia_ok = agua.validar_valencia()
    print(f"Valência válida?   {valencia_ok}")
    print()
    
    # Exibe os vizinhos de um átomo (átomos conectados e tipo de ligação)
    vizinhos_O = agua.obter_vizinhos(oxigenio)
    print(f"Vizinhos do oxigênio:")
    for vizinho, ordem in vizinhos_O:
        print(f"  - {vizinho} (ligação de ordem {ordem})")
    print()
    
    # Exibe o grau (valência aparente) de um átomo
    print(f"Grau do oxigênio: {agua.obter_grau(oxigenio)}")
    print(f"Grau do H#1:      {agua.obter_grau(atomos_H[0])}")
    print()
    
    # Exibe representação formatada da molécula
    print(f"Molécula: {agua}")
    print()
    
    # =========================================================================
    # PARTE 3: Molécula de Metano (CH4)
    # =========================================================================
    print("3. MOLÉCULA DE METANO (CH4)")
    print("-" * 70)
    
    metano = Molecula("Metano")
    
    # Adiciona 1 carbono e 4 hidrogênios
    metano.adicionar_elemento(C, 1)  # id: 4
    metano.adicionar_elemento(H, 4)  # ids: 5, 6, 7, 8
    
    print(f"Átomos: {[str(a) for a in metano.atomos]}")
    print()
    
    # Recupera o carbono e os hidrogênios
    carbono = [a for a in metano.atomos if a.elemento == C][0]
    h_metano = [a for a in metano.atomos if a.elemento == H]
    
    print(f"Carbono: {carbono}")
    print(f"Hidrogênios: {[str(h) for h in h_metano]}")
    print()
    
    # Adiciona ligações: carbono conectado a cada hidrogênio
    for h in h_metano:
        metano.adicionar_ligacao(carbono, h, 1)
    
    print(f"Ligações adicionadas:")
    for lig in metano.ligacoes:
        print(f"  - {lig}")
    print()
    
    print(f"Fórmula molecular: {metano.exibir_formula()}")
    print(f"Massa molecular:   {metano.calcular_massa_molecular():.3f} u")
    print(f"Composição:        {metano.calcular_composicao()}")
    print(f"Valência válida?   {metano.validar_valencia()}")
    print()
    
    print(f"Vizinhos do carbono:")
    for vizinho, ordem in metano.obter_vizinhos(carbono):
        print(f"  - {vizinho} (ordem {ordem})")
    print()
    
    print(f"Grau do carbono: {metano.obter_grau(carbono)}")
    print()
    
    print(f"Molécula: {metano}")
    print()
    
    # =========================================================================
    # PARTE 4: Molécula de Etanol (C2H6O) - Estrutura: CH3-CH2-OH
    # =========================================================================
    print("4. MOLÉCULA DE ETANOL (C2H6O)")
    print("-" * 70)
    
    etanol = Molecula("Etanol")
    
    # Adiciona elementos
    etanol.adicionar_elemento(C, 2)  # ids: 9, 10
    etanol.adicionar_elemento(H, 6)  # ids: 11, 12, 13, 14, 15, 16
    etanol.adicionar_elemento(O, 1)  # id: 17
    
    print(f"Átomos totais: {len(etanol.atomos)}")
    print()
    
    # Recupera os átomos
    carbonos = [a for a in etanol.atomos if a.elemento == C]
    h_etanol = [a for a in etanol.atomos if a.elemento == H]
    oxigenio_etanol = [a for a in etanol.atomos if a.elemento == O][0]
    
    print(f"Carbonos:  {[str(c) for c in carbonos]}")
    print(f"Oxigênio:  {oxigenio_etanol}")
    print()
    
    # Estrutura: CH3-CH2-OH
    # Ligação C-C
    etanol.adicionar_ligacao(carbonos[0], carbonos[1], 1)
    
    # Primeiro carbono conectado a 3 hidrogênios
    for i in range(3):
        etanol.adicionar_ligacao(carbonos[0], h_etanol[i], 1)
    
    # Segundo carbono conectado a 2 hidrogênios
    for i in range(3, 5):
        etanol.adicionar_ligacao(carbonos[1], h_etanol[i], 1)
    
    # Oxigênio conectado ao segundo carbono
    etanol.adicionar_ligacao(carbonos[1], oxigenio_etanol, 1)
    
    # Oxigênio conectado a 1 hidrogênio (grupo OH)
    etanol.adicionar_ligacao(oxigenio_etanol, h_etanol[5], 1)
    
    print(f"Ligações adicionadas: {len(etanol.ligacoes)}")
    print()
    
    print(f"Fórmula molecular: {etanol.exibir_formula()}")
    print(f"Massa molecular:   {etanol.calcular_massa_molecular():.3f} u")
    print(f"Composição:        {etanol.calcular_composicao()}")
    print(f"Valência válida?   {etanol.validar_valencia()}")
    print()
    
    print(f"Molécula: {etanol}")
    print()
    
    # =========================================================================
    # RESUMO FINAL
    # =========================================================================
    print("=" * 70)
    print("RESUMO DAS MOLÉCULAS CRIADAS")
    print("=" * 70)
    print(f"1. {agua}")
    print(f"2. {metano}")
    print(f"3. {etanol}")
    print()


if __name__ == "__main__":
    main()
