"""
Classe Atomo - Representa um átomo individual dentro de uma molécula.
Cada átomo tem um identificador único global gerado automaticamente.
"""

from elemento import Elemento


class Atomo:
    """
    Representa um átomo individual em uma molécula.
    Cada instância recebe um ID único sequencial.
    
    Atributos:
        elemento (Elemento): O elemento químico deste átomo
        id (int): Identificador único gerado automaticamente
    """
    
    # Atributo de classe: contador para gerar IDs únicos
    _proximo_id = 1
    
    def __init__(self, elemento):
        """
        Inicializa um átomo com um elemento e atribui um ID único.
        
        Args:
            elemento (Elemento): Uma instância da classe Elemento
            
        Raises:
            TypeError: Se elemento não é uma instância de Elemento
        """
        if not isinstance(elemento, Elemento):
            raise TypeError("Elemento deve ser uma instância da classe Elemento")
        
        # Atribui o elemento (somente leitura)
        self._elemento = elemento
        
        # Atribui ID único e incrementa o contador
        self._id = Atomo._proximo_id
        Atomo._proximo_id += 1
    
    @property
    def elemento(self):
        """Retorna o elemento químico deste átomo."""
        return self._elemento
    
    @property
    def id(self):
        """Retorna o identificador único deste átomo."""
        return self._id
    
    def __str__(self):
        """
        Retorna representação do átomo no formato: símbolo#id
        Ex: "H#1", "C#5", "O#3"
        """
        return f"{self._elemento.simbolo}#{self._id}"
    
    def __repr__(self):
        """Representação técnica - igual ao __str__."""
        return self.__str__()
    
    def resetar_contador(cls):
        """
        Método de classe para resetar o contador de IDs.
        Útil para testes, mas não deve ser usado em produção.
        """
        Atomo._proximo_id = 1
