from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Step 1: Create a circuit with 1 qubit and 1 classical bit (to store the measurement)
qc = QuantumCircuit(1, 1)

# Step 2: Apply Hadamard gate -> puts qubit into superposition
qc.h(0)

# Step 3: Measure the qubit, store result in classical bit
qc.measure(0, 0)

# Step 4: Draw the circuit (see what you built)
print(qc.draw())

# Step 5: Run it on a simulator, 1000 times, to see the distribution
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)  # should be close to {'0': 500, '1': 500}