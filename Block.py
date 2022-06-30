"""
class Block:
    def __init__(self, index, transactions , timestamp ):
        self.index          = []
        self.transactions   = transactions
        self.timestamp      = timestamp
"""


"""
#Añadimos la fórmula para calcular el hash del bloque 

from hashlib import sha256
import json


class Block:
    def __init__(self, index, transactions , timestamp ):
        self.index          = []
        self.transactions   = transactions
        self.timestamp      = timestamp

    def compute_hash(block):
        """
        Una función que crea el hash del bloque.
        """


        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


"""

#Añadimos en el bloque, el hash del bloque anterior para asegurar que no estamos manipulando los bloques anteriores,
# ya que cualquier cambio en el bloque anterior invalidará la cadena entera.

from hashlib import sha256
import json


class Block:
    def __init__(self, index, transactions , timestamp , previous_hash):
        self.index          = []
        self.transactions   = transactions
        self.timestamp      = timestamp
        self.previous_hash  = previous_hash

    def compute_hash(block):
        """
        Una función que crea el hash del bloque.
        """


        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


