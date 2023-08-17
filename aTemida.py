import hashlib # importando biblioteca de gerador de hash

def hashGenerator(data):
    result = hashlib.sha256(data.encode()) # convete dados para hexadecimal
    return result.hexdigest() # retorna resultado em hexadecimal


class Block:
    def __init__(self, data, hash, prev_hash): #nessa função temos self, dados, o codigo hash e o hash anterior
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('last_gen') #hashLast recebe a forma hexadecimal do código hash
        hashFirst = hashGenerator('first_gen') #hashFirst recebe a forma hexadecimal do código hash

        genesis = Block('gen_data',hashFirst, hashLast) # criando bloco genesis(começo)
        self.chain = [genesis] # crinando corrente do bloco genesis

    def add_block(self, data): # função para adicionar um novo bloco na bolochain
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data+prev_hash)
        block = Block(data, hash, prev_hash) # eliminando a minima chance dos hash serem parecidos
        self.chain.append(block) # anexa o novo bloco na blockchain


blch = Blockchain() # criando objeto da classe Blockchain
blch.add_block('A') # criando primeiro bloco
blch.add_block('B') # criando segundo bloco
blch.add_block('C') # criando terceiro bloco

for block  in blch.chain: # foreach, para cada bloco que criarmos, será corvertido em dicionario
    print(block.__dict__) # printa o bloco da blockchain