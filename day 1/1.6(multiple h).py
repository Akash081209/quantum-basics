from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
qc.h(0)
qc.h(0)
qc.h(0)
qc.h(0)
qc.measure(0,0)
print(qc.draw())

simulator = AerSimulator()
result = simulator.run(qc, shots=100).result()
print(result.get_counts())

#When we use two H gates it comes to 0 again like after typing first qc.h(0) it comes in superposistion 50/50 in correct equator,
#after typing second time  qc.h(0) it comes to 0 again like it minusm itself 
#doing it for third time it comes to superposition again