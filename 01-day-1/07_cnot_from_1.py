from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)   # 2 qubits, 2 classical bits

qc.x(0)                     # flip q0 from 0 to 1
qc.cx(0, 1)                 # CNOT: q0 = control, q1 = target
qc.measure([0, 1], [0, 1])  # measure both qubits

print(qc.draw())

simulator = AerSimulator()
result=simulator.run(qc,shots = 1000).result()
counts=result.get_counts()
print(counts)

