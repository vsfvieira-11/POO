"""
Classe Ligacao - Representa uma ligação covalente entre dois átomos.
Suporta ligações simples (1), duplas (2) e triplas (3).
"""

from atomo import Atomo


class Ligacao:
    """
    Representa uma ligação covalente entre dois átomos individuais.
    
    Atributos:
        atomo1 (Atomo): Primeiro átomo da ligação
        atomo2 (Atomo): Segundo átomo da ligação
        ordem (int): Tipo de ligação (1=simples, 2=dupla, 3=tripla)
    """
    
    # Dicionário para converter ordem em símbolo visual
    _simbolos_ligacao = {
        1: "-",
        2: "=",
        3: "≡"
    }
    
    # Dicionário para converter ordem em nome textual
    _nomes_ligacao = {
        1: "simples",
        2: "dupla",
        3: "tripla"
    }
    
    def __init__(self, atomo1, atomo2, ordem=1):
        """
        Inicializa uma ligação entre dois átomos com validações.
        
        Args:
            atomo1 (Atomo): Primeiro átomo
            atomo2 (Atomo): Segundo átomo
            ordem (int): Ordem da ligação (1, 2 ou 3). Padrão: 1
            
        Raises:
            TypeError: Se os átomos não são instâncias de Atomo
            ValueError: Se os átomos são iguais ou ordem é inválida
        """
        # Validação de tipo
        if not isinstance(atomo1, Atomo):
            raise TypeError("atomo1 deve ser uma instância de Atomo")
        if not isinstance(atomo2, Atomo):
            raise TypeError("atomo2 deve ser uma instância de Atomo")
        
        # Validação: os átomos não podem ser o mesmo
        if atomo1.id == atomo2.id:
            raise ValueError("Os dois átomos não podem ser o mesmo objeto")
        
        # Validação de ordem
        if ordem not in [1, 2, 3]:
            raise ValueError("Ordem da ligação deve ser 1 (simples), 2 (dupla) ou 3 (tripla)")
        
        # Atribuição
        self._atomo1 = atomo1
        self._atomo2 = atomo2
        self._ordem = ordem
    
    @property
    def atomo1(self):
        """Retorna o primeiro átomo da ligação."""
        return self._atomo1
    
    @property
    def atomo2(self):
        """Retorna o segundo átomo da ligação."""
        return self._atomo2
    
    @property
    def ordem(self):
        """Retorna a ordem da ligação (1, 2 ou 3)."""
        return self._ordem
    
    def get_outro_atomo(self, atomo):
        """
        Dado um átomo, retorna o outro átomo desta ligação.
        
        Args:
            atomo (Atomo): Um dos átomos da ligação
            
        Returns:
            Atomo: O outro átomo da ligação, ou None se atomo não participa
        """
        if atomo.id == self._atomo1.id:
            return self._atomo2
        elif atomo.id == self._atomo2.id:
            return self._atomo1
        else:
            return None
    
    def __str__(self):
        """
        Retorna representação formatada da ligação.
        Ex: "H#1 - O#2 (simples)" ou "C#3 ≡ C#4 (tripla)"
        """
        simbolo = self._simbolos_ligacao.get(self._ordem, "-")
        nome = self._nomes_ligacao.get(self._ordem, "desconhecida")
        return f"{self._atomo1} {simbolo} {self._atomo2} ({nome})"
    
    def __repr__(self):
        """Representação técnica da ligação."""
        return f"Ligacao({self._atomo1}, {self._atomo2}, ordem={self._ordem})"
