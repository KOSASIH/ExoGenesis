import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def __repr__(self):
        return f"Block({self.index}, {self.previous_hash}, {self.timestamp}, {self.data}, {self.hash})"

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block", ""))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data, "")
    return Block(index, previous_block.hash, timestamp, data, hash)

def calculate_hash(index, previous_hash, timestamp, data, hash_input):
    block_data = str(index) + previous_hash + str(timestamp) + data + hash_input
    return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data, ""):
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

    return True

def add_block_to_blockchain(blockchain, new_block):
    if isinstance(new_block, Block):
        blockchain.append(new_block)
    else:
        raise TypeError("new_block must be of type Block")

def integrateBlockchainForResourceTracking(resource_data):
    """
    Integrates blockchain technology for tracking the ownership and transfer of space resources.
    
    Parameters:
    resource_data (list of tuples): A list of tuples containing the resource name, owner, and quantity.
    
    Returns:
    blockchain (list of Blocks): A blockchain containing the ownership and transfer history of the space resources.
    """
    
    # Create the genesis block
    genesis_block = create_genesis_block()

    # Initialize the blockchain with the genesis block
    blockchain = [genesis_block]

    # Add each resource to the blockchain
    for resource in resource_data:
        resource_name, owner, quantity = resource
        new_block = create_new_block(blockchain[-1], f"{resource_name}: {owner}: {quantity}")
        add_block_to_blockchain(blockchain, new_block)

    # Validate the blockchain
    if not validate_blockchain(blockchain):
        raise ValueError("Blockchain is invalid")

    return blockchain
