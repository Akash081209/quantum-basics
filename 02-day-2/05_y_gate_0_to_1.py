from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc =  QuantumCircuit(1,1)

qc.y(0)#it flips the q0 value from 0 to 1 and also the sign it is + so it turns it into -
#it only measure value not signs so it will print 1 not -1 

qc.measure(0,0)

print(qc.draw())

simulator = AerSimulator()
result=simulator.run(qc,shots = 1000).result()
counts=result.get_counts()
print(counts)
