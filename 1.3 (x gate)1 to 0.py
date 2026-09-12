from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
qc.x(0) # so it flips 0 to 1
qc.x(0)   #this flips 1 to 0 what i wanted     
qc.measure(0,0)

print(qc.draw())

simulator= AerSimulator()
result = simulator.run(qc, shots=1000).result()
print(result.get_counts())