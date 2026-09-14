from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
qc.h(0)
qc.s(0)
qc.s(0)
qc.h(0)

qc.measure(0,0)
print(qc.draw())

simulator = AerSimulator()
result=simulator.run(qc,shots = 1000).result()
counts=result.get_counts()
print(counts)