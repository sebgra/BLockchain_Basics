import hashlib

class NeuralCoinBlock:

	def __init__(self, previous_block_hash, transaction_list):

		self.previous_block_hash = previous_block_hash
		self.transaction_list = transaction_list

		self.block_data = "-".join(transaction_list) + "-" + self.previous_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



t1 = "A sends 4.6 NC to B"
t2 = "A sends 2.8 NC to C"
t3 = "B sends 0.2 NC to A"
t4 = "C sends 10.4 NC to B"
t5 = "B sends 1.1 NC to A"


initial_block = NeuralCoinBlock("Initial String", [t1,t2])

print(f"Initial block data : {initial_block.block_data}")
print(f"Initial block hash : {initial_block.block_hash}")

second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(f"Second block data : {second_block.block_data}")
print(f"Second block hash : {second_block.block_hash}")

third_block = NeuralCoinBlock(second_block.block_hash, [t5])

print(f"Third block data : {third_block.block_data}")
print(f"Third block hash : {third_block.block_hash}")