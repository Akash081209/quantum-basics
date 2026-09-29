from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)   # 2 qubits, 2 classical bits
qc.h(0)                     # put qubit 0 into superposition
qc.cx(0, 1)                 # CNOT: qubit 0 = control, qubit 1 = target
qc.measure([0, 1], [0, 1])  # measure both qubits

print(qc.draw())

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
print(result.get_counts())
