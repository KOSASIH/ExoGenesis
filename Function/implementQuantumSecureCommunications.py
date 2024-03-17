import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

def implementQuantumSecureCommunications(sender_data, receiver_data):
    """
    Implement Quantum Secure Communications using Quantum Key Distribution (QKD) and Quantum Teleportation.
    
    Parameters:
    sender_data (list): List of bits to be sent by the sender.
    receiver_data (list): List of bits to be received by the receiver.
    
    Returns:
    tuple: A tuple containing the shared secret key and the received data.
    """
    
    # Define the quantum circuit for Quantum Key Distribution (QKD)
    qkd_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    qkd_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    qkd_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    qkd_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    qkd_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    qkd_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    qkd_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    qkd_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    qkd_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    qkd_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    qkd_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum Teleportation
    teleportation_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    teleportation_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    teleportation_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    teleportation_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    teleportation_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    teleportation_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    teleportation_circuit.cx(0uit.cx(0, 2)
    
    # Measure the first and second qubits
    qkd_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum Teleportation
    teleportation_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    teleportation_circuit.h(0)
    
    #, 1)
    
    # Apply the CNOT gate to the second and third qubits
    teleportation_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    teleportation_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    teleportation_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    teleportation_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx Apply the C(0, 1)
    
    # Apply the CNOT gate to the first and third qubitsNOT gate to the first and second qubits
    teleportation_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    teleportation_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    teleportation_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    teleportation_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    teleportation_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    teleportation_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    teleportation_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    teleportation_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    teleportation_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubitsstate_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the thirdqubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to thefirst and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOTgate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
# Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
   # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Measure the first and second qubits
    state_transfer_circuit.measure([0, 1], [0, 1])
    
    # Define the quantum circuit for Quantum State Transfer
    state_transfer_circuit = QuantumCircuit(3, 2)
    
    # Apply the Hadamard gate to the first qubit
    state_transfer_circuit.h(0)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0, 2)
    
    # Apply the Hadamard gate to the second qubit
    state_transfer_circuit.h(1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the CNOT gate to the first and second qubits
    state_transfer_circuit.cx(0, 1)
    
    # Apply the CNOT gate to the second and third qubits
    state_transfer_circuit.cx(1, 2)
    
    # Apply the Hadamard gate to the third qubit
    state_transfer_circuit.h(2)
    
    # Apply the CNOT gate to the first and third qubits
    state_transfer_circuit.cx(0The provided code is incorrect because it repeats the same circuit twice. The correct code for Quantum State Transfer (QST) should be as follows:

```python
from qiskit import QuantumCircuit

# Define the quantum circuit for Quantum State Transfer
state_transfer_circuit = QuantumCircuit(3, 2)

# Apply the Hadamard gate to the first qubit
state_transfer_circuit.h(0)

# Apply the CNOT gate to the first and second qubits
state_transfer_circuit.cx(0, 1)

# Apply the CNOT gate to the first and third qubits
state_transfer_circuit.cx(0, 2)

# Apply the Hadamard gate to the second qubit
state_transfer_circuit.h(1)

# Apply the CNOT gate to the second and third qubits
state_transfer_circuit.cx(1, 2)

# Apply the CNOT gate to the first and second qubits
state_transfer_circuit.cx(0, 1)

# Apply the CNOT gate to the second and third qubits
state_transfer_circuit.cx(1, 2)

# Apply the Hadamard gate to the third qubit
state_transfer_circuit.h(2)

# Apply the CNOT gate to the first and third qubits
state_transfer_circuit.cx(0, 2)

# Measure the first and second qubits
state_transfer_circuit.measure([0, 1], [0, 1])
