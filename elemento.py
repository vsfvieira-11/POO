"""
Classe Elemento - Representa um elemento químico da tabela periódica.
Elementos são imutáveis e hashable, podendo ser usados como chaves de dicionário.
"""


class Elemento:
    """
    Representa um elemento químico com suas propriedades básicas.
    
    Atributos:
        simbolo (str): Símbolo do elemento (ex: "H", "O", "C")
        nome (str): Nome do elemento (ex: "Hidrogênio", "Oxigênio")
        numero_atomico (int): Número de prótons (Z)
        massa_atomica (float): Massa em unidades de massa atômica (u)
        valencia_maxima (int): Número máximo de ligações covalentes
    """
    
    def __init__(self, simbolo, nome, numero_atomico, massa_atomica, valencia_maxima):
        """
        Inicializa um elemento com validação de todas as propriedades.
        
        Args:
            simbolo (str): 1 ou 2 letras, primeira maiúscula
            nome (str): Nome do elemento
            numero_atomico (int): Deve ser > 0
            massa_atomica (float): Deve ser > 0
            valencia_maxima (int): Entre 1 e 8
            
        Raises:
            ValueError: Se alguma validação falhar
            TypeError: Se tipo de dado for incorreto
        """
        # Validação de tipo
        if not isinstance(simbolo, str):
            raise TypeError("Símbolo deve ser uma string")
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser uma string")
        if not isinstance(numero_atomico, int):
            raise TypeError("Número atômico deve ser inteiro")
        if not isinstance(massa_atomica, (int, float)):
            raise TypeError("Massa atômica deve ser numérica")
        if not isinstance(valencia_maxima, int):
            raise TypeError("Valência máxima deve ser inteira")
        
        # Validação de símbolo: 1 ou 2 letras, primeira maiúscula
        if len(simbolo) < 1 or len(simbolo) > 2:
            raise ValueError("Símbolo deve ter 1 ou 2 letras")
        if not simbolo[0].isupper():
            raise ValueError("Primeira letra do símbolo deve ser maiúscula")
        if not simbolo.isalpha():
            raise ValueError("Símbolo deve conter apenas letras")
        
        # Validação de número atômico
        if numero_atomico <= 0:
            raise ValueError("Número atômico deve ser maior que 0")
        
        # Validação de massa atômica
        if massa_atomica <= 0:
            raise ValueError("Massa atômica deve ser maior que 0")
        
        # Validação de valência
        if valencia_maxima < 1 or valencia_maxima > 8:
            raise ValueError("Valência máxima deve estar entre 1 e 8")
        
        # Atribuição de valores (imutável)
        self._simbolo = simbolo
        self._nome = nome
        self._numero_atomico = numero_atomico
        self._massa_atomica = massa_atomica
        self._valencia_maxima = valencia_maxima
    
    @property
    def simbolo(self):
        """Retorna o símbolo do elemento."""
        return self._simbolo
    
    @property
    def nome(self):
        """Retorna o nome do elemento."""
        return self._nome
    
    @property
    def numero_atomico(self):
        """Retorna o número atômico."""
        return self._numero_atomico
    
    @property
    def massa_atomica(self):
        """Retorna a massa atômica."""
        return self._massa_atomica
    
    @property
    def valencia_maxima(self):
        """Retorna a valência máxima."""
        return self._valencia_maxima
    
    def __str__(self):
        """
        Retorna representação formatada do elemento.
        Ex: "H (Hidrogênio): Z=1, massa=1.008 u, valência=1"
        """
        return (f"{self._simbolo} ({self._nome}): Z={self._numero_atomico}, "
                f"massa={self._massa_atomica} u, valência={self._valencia_maxima}")
    
    def __repr__(self):
        """Representação técnica do elemento."""
        return f"Elemento('{self._simbolo}', '{self._nome}', {self._numero_atomico})"
    
    def __hash__(self):
        """
        Retorna o hash baseado no símbolo.
        Permite usar elementos como chaves de dicionário.
        """
        return hash(self._simbolo)
    
    def __eq__(self, other):
        """
        Dois elementos são iguais se têm o mesmo símbolo.
        """
        if not isinstance(other, Elemento):
            return False
        return self._simbolo == other._simbolo
