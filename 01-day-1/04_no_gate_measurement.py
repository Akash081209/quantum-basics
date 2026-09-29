#here in quantum computing, the default is 0,so if you don't apply any gates,
# the qubit will remain in the |0> state. This means that when you measure it, you will always get 0.
#example of a quantum circuit with no gates applied, which will always measure 0.
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
qc.measure(0,0)

print(qc.draw())

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
print(result.get_counts())



