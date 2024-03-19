import hashlib
import time

class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = None
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.id}{self.data}{self.timestamp}{self.previous_hash}".encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return f"Node({self.id}, {self.data}, {self.timestamp}, {self.previous_hash}, {self.hash})"


class DecentralizedNetworkInfrastructure:
    def __init__(self):
        self.nodes = []

    def add_node(self, data):
        if not self.nodes:
            node = Node(0, data)
        else:
            node = Node(len(self.nodes), data, self.nodes[-1].timestamp + 1)
            node.previous_hash = self.nodes[-1].hash
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    def validate_network(self):
        for i in range(1, len(self.nodes)):
            if self.nodes[i].hash != self.nodes[i].calculate_hash():
                return False
            if self.nodes[i].previous_hash != self.nodes[i - 1].hash:
                return False
        return True


def main():
    dni = DecentralizedNetworkInfrastructure()
    dni.add_node("Hello, World!")
    dni.add_node("This is a decentralized network infrastructure.")
    dni.add_node("We can add nodes and validate the network.")
    print(dni.get_nodes())
    print(dni.validate_network())


if __name__ == "__main__":
    main()
