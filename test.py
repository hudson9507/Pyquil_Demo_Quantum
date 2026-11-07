from pyquil import Program
from pyquil.gates import H, CNOT

# Create a quantum circuit
circuit = Program()

# Put qubit 0 into superposition
circuit += H(0)

# Entangle qubits 0 and 1
circuit += CNOT(0, 1)

print(circuit)