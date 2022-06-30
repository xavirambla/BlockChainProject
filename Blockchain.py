"""
class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions =[] # información para insertar en el blockchain
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Una función para generar el bloque génesis (el primero) y añadirlo a la cadena.
        El bloque tiene index 0, previous_hash 0 y un hash válido.

        """
        genesis_block = Block(0,[],time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)


    #property
    def last_block(self):
        return self.chain[-1]
"""

"""
Ahora el problema tenemos que  cualquiera puede coger y modificar un bloque anterior y recalcular hashes de los siguientes bloques
Conseguiriamos un nuevo blockchain diferente pero válido.

Para arreglarlo , agregaremos una condición al hash, es decir , aceptaremos únicamente los hashes que cumplan con dicha condicion.
Por ejemplo, nuestro hash debería empezar por dos 0s

Añadimos el campo nonce, que es un número que cambiará constantemente hasta que obtengamos un hash que satifsaga la condición.
El número de 0s prefijados decide la 'dificultad' de nuestro algoritmo.



"""
"""
class Blockchain:
    difficulty = 2   # Dificultad del algoritmo de prueba de trabajo.

    def __init__(self):
        self.unconfirmed_transactions =[] # información para insertar en el blockchain
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        #Una función para generar el bloque génesis (el primero) y añadirlo a la cadena.
        #El bloque tiene index 0, previous_hash 0 y un hash válido.

        
        genesis_block = Block(0,[],time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    #property
    def last_block(self):
        return self.chain[-1]


    def proof_of_work(self, block):
#        Función que intenta distintos valores de nonce hasta obtener
 #       un hash que satisfaga nuestro criterio de dificultad.

        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash


"""
class Blockchain:
    difficulty = 2   # Dificultad del algoritmo de prueba de trabajo.

    def __init__(self):
        self.unconfirmed_transactions =[] # información para insertar en el blockchain
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        #Una función para generar el bloque génesis (el primero) y añadirlo a la cadena.
        #El bloque tiene index 0, previous_hash 0 y un hash válido.


        genesis_block = Block(0,[],time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    #property
    def last_block(self):
        return self.chain[-1]


    def proof_of_work(self, block):
#        Función que intenta distintos valores de nonce hasta obtener
 #       un hash que satisfaga nuestro criterio de dificultad.

        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash


def add_block(self, block, proof):
    #   Una función que agrega el bloque a la cadena luego de la verificación.

    previous_hash = self.last_block.hash

    if previous_hash != block.previous_hash:
        return False

    if not self.is_valid_proof(block, proof):
        return False

    block.hash = proof
    self.chain.append(block)
    return True


    def is_valid_proof(self, block, block_hash):
        # Chequear si block_hash es un hash válido y satisface nuestro
        # criterio de dificultad.
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

