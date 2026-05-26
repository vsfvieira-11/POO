"""
Classe Molecula - Gerencia uma coleção de átomos e ligações químicas.
Calcula automaticamente composição, massa e fórmula molecular.
"""

from elemento import Elemento
from atomo import Atomo
from ligacao import Ligacao


class Molecula:
    """
    Representa uma molécula como uma coleção de átomos e ligações.
    A composição é derivada automaticamente da lista de átomos.
    
    Atributos:
        nome (str): Nome comum da molécula
        atomos (list): Lista de instâncias de Atomo
        ligacoes (list): Lista de instâncias de Ligacao
    """
    
    def __init__(self, nome):
        """
        Inicializa uma molécula vazia com um nome.
        
        Args:
            nome (str): Nome comum da molécula (ex: "Água", "Metano")
        """
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser uma string")
        
        self._nome = nome
        self._atomos = []
        self._ligacoes = []
    
    @property
    def nome(self):
        """Retorna o nome da molécula."""
        return self._nome
    
    @property
    def atomos(self):
        """Retorna a lista de átomos."""
        return self._atomos
    
    @property
    def ligacoes(self):
        """Retorna a lista de ligações."""
        return self._ligacoes
    
    def adicionar_elemento(self, elemento, quantidade=1):
        """
        Cria e adiciona quantidade novos átomos de um elemento.
        Cada novo átomo recebe um ID único automaticamente.
        
        Args:
            elemento (Elemento): O elemento a adicionar
            quantidade (int): Quantos átomos criar. Padrão: 1
            
        Raises:
            TypeError: Se elemento não é uma instância de Elemento
            ValueError: Se quantidade <= 0
        """
        if not isinstance(elemento, Elemento):
            raise TypeError("Elemento deve ser uma instância de Elemento")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que 0")
        
        # Cria 'quantidade' novos átomos
        for _ in range(quantidade):
            novo_atomo = Atomo(elemento)
            self._atomos.append(novo_atomo)
    
    def remover_atomo(self, atomo):
        """
        Remove um átomo específico da molécula.
        Também remove todas as ligações em que ele participa.
        
        Args:
            atomo (Atomo): O átomo a remover
            
        Raises:
            ValueError: Se o átomo não pertence a esta molécula
        """
        # Verifica se o átomo existe
        if atomo not in self._atomos:
            raise ValueError("Átomo não pertence a esta molécula")
        
        # Remove o átomo
        self._atomos.remove(atomo)
        
        # Remove todas as ligações que envolvem este átomo
        self._ligacoes = [
            lig for lig in self._ligacoes 
            if lig.atomo1.id != atomo.id and lig.atomo2.id != atomo.id
        ]
    
    def adicionar_ligacao(self, atomo1, atomo2, ordem=1):
        """
        Adiciona uma ligação entre dois átomos.
        Verifica se ambos pertencem a esta molécula e evita duplicatas.
        
        Args:
            atomo1 (Atomo): Primeiro átomo
            atomo2 (Atomo): Segundo átomo
            ordem (int): Tipo de ligação (1, 2 ou 3). Padrão: 1
            
        Raises:
            ValueError: Se algum átomo não pertence à molécula ou ligação já existe
            TypeError: Se algum parâmetro tem tipo incorreto
        """
        if not isinstance(atomo1, Atomo) or not isinstance(atomo2, Atomo):
            raise TypeError("Ambos os parâmetros devem ser instâncias de Atomo")
        
        # Verifica se ambos os átomos pertencem à molécula
        if atomo1 not in self._atomos:
            raise ValueError("atomo1 não pertence a esta molécula")
        if atomo2 not in self._atomos:
            raise ValueError("atomo2 não pertence a esta molécula")
        
        # Verifica se a ligação já existe (na mesma ordem)
        for lig in self._ligacoes:
            if ((lig.atomo1.id == atomo1.id and lig.atomo2.id == atomo2.id and lig.ordem == ordem) or
                (lig.atomo1.id == atomo2.id and lig.atomo2.id == atomo1.id and lig.ordem == ordem)):
                raise ValueError("Ligação já existe com esta ordem")
        
        # Cria e adiciona a nova ligação
        nova_ligacao = Ligacao(atomo1, atomo2, ordem)
        self._ligacoes.append(nova_ligacao)
    
    def calcular_composicao(self):
        """
        Calcula a composição molecular (quantidades de cada elemento).
        
        Returns:
            dict: Dicionário {Elemento: quantidade}
        """
        composicao = {}
        
        for atomo in self._atomos:
            elemento = atomo.elemento
            if elemento in composicao:
                composicao[elemento] += 1
            else:
                composicao[elemento] = 1
        
        return composicao
    
    def calcular_massa_molecular(self):
        """
        Calcula a massa molecular total.
        
        Returns:
            float: Massa em unidades de massa atômica (u)
        """
        composicao = self.calcular_composicao()
        massa_total = 0
        
        for elemento, quantidade in composicao.items():
            massa_total += elemento.massa_atomica * quantidade
        
        return massa_total
    
    def exibir_formula(self):
        """
        Gera a fórmula molecular.
        Ordem: Carbono, Hidrogênio, depois demais em ordem alfabética.
        
        Returns:
            str: Fórmula molecular (ex: "H2O", "C6H12O6")
        """
        composicao = self.calcular_composicao()
        
        # Separa os elementos em categorias
        carbono = None
        hidrogenio = None
        outros = {}
        
        for elemento, quantidade in composicao.items():
            if elemento.simbolo == "C":
                carbono = (elemento, quantidade)
            elif elemento.simbolo == "H":
                hidrogenio = (elemento, quantidade)
            else:
                outros[elemento.simbolo] = (elemento, quantidade)
        
        # Constrói a fórmula na ordem especificada
        formula = ""
        
        # Adiciona Carbono
        if carbono:
            elem, qtd = carbono
            formula += elem.simbolo
            if qtd > 1:
                formula += str(qtd)
        
        # Adiciona Hidrogênio
        if hidrogenio:
            elem, qtd = hidrogenio
            formula += elem.simbolo
            if qtd > 1:
                formula += str(qtd)
        
        # Adiciona demais em ordem alfabética
        for simbolo in sorted(outros.keys()):
            elem, qtd = outros[simbolo]
            formula += elem.simbolo
            if qtd > 1:
                formula += str(qtd)
        
        return formula
    
    def obter_vizinhos(self, atomo):
        """
        Retorna uma lista de vizinhos (átomos conectados) e a ordem de cada ligação.
        
        Args:
            atomo (Atomo): O átomo central
            
        Returns:
            list: Lista de tuplas (atomo_vizinho, ordem_ligacao)
        """
        vizinhos = []
        
        for ligacao in self._ligacoes:
            outro_atomo = ligacao.get_outro_atomo(atomo)
            if outro_atomo is not None:
                vizinhos.append((outro_atomo, ligacao.ordem))
        
        return vizinhos
    
    def obter_grau(self, atomo):
        """
        Calcula o grau (ou valência aparente) de um átomo.
        É a soma das ordens de todas as ligações que incidem nele.
        
        Args:
            atomo (Atomo): O átomo
            
        Returns:
            int: Soma das ordens das ligações
        """
        grau = 0
        
        for ligacao in self._ligacoes:
            if ligacao.atomo1.id == atomo.id or ligacao.atomo2.id == atomo.id:
                grau += ligacao.ordem
        
        return grau
    
    def validar_valencia(self):
        """
        Valida a regra de valência: cada átomo respeita sua valência máxima.
        
        Returns:
            bool: True se todos os átomos respeitam a valência, False caso contrário
        """
        for atomo in self._atomos:
            grau = self.obter_grau(atomo)
            valencia_max = atomo.elemento.valencia_maxima
            
            if grau > valencia_max:
                print(f"AVISO: {atomo} viola a valência "
                      f"(grau={grau}, máximo={valencia_max})")
                return False
        
        return True
    
    def __str__(self):
        """
        Retorna representação formatada da molécula.
        Ex: "Água: H2O, massa=18.008 u, 3 átomos, 2 ligações"
        """
        formula = self.exibir_formula()
        massa = self.calcular_massa_molecular()
        num_atomos = len(self._atomos)
        num_ligacoes = len(self._ligacoes)
        
        return (f"{self._nome}: {formula}, massa={massa:.3f} u, "
                f"{num_atomos} átomos, {num_ligacoes} ligações")
    
    def __repr__(self):
        """Representação técnica da molécula."""
        return f"Molecula('{self._nome}', {len(self._atomos)} átomos, {len(self._ligacoes)} ligações)"
