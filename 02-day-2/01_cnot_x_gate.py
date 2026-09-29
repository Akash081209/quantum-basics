from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc=QuantumCircuit(2,2)

qc.x(0)# flips q0 from default 0 to 1
qc.cx(0, 1)# q0=control qubit q1= target
qc.measure(0, 0)
qc.measure(1, 1)

print(qc.draw())
simulator = AerSimulator()
result=simulator.run(qc,shots = 1000).result()
counts=result.get_counts()
print(counts)

