import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Block: \nTimestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}\n"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Usage example
my_blockchain = Blockchain()

# Adding blocks to the blockchain
my_blockchain.add_block(Block(time.time(), {"amount": 5}, ""))
my_blockchain.add_block(Block(time.time(), {"amount": 10}, ""))
my_blockchain.add_block(Block(time.time(), {"amount": 15}, ""))

# Checking if the blockchain is valid
print("Is blockchain valid? ", my_blockchain.is_chain_valid())

# Modifying the data of a block
my_blockchain.chain[1].data = {"amount": 100}

# Checking if the modified blockchain is valid
print("Is modified blockchain valid? ", my_blockchain.is_chain_valid())
