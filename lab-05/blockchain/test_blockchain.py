from blockchain import Blockchain

my_blockchain = Blockchain()

my_blockchain.add_transaction(sender="Alice", receiver="Bob", amount=10)
my_blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=5)
my_blockchain.add_transaction(sender="Charlie", receiver="Alice", amount=3)

previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction(sender="Genesis", receiver="Miner", amount=1)
new_block = my_blockchain.create_block(proof=new_proof, previous_hash=previous_hash)

for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Proof: {block.proof}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-------------------------------")
    
print("Is the blockchain valid?", my_blockchain.is_chain_valid(my_blockchain.chain))