from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2,2)
qc.x(0)# flips 0 to 1 
qc.x(0)#flips that again 1 to 0
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)

print(qc.draw())
simulator = AerSimulator()
result=simulator.run(qc,shots = 1000).result()
counts=result.get_counts()
print(counts)