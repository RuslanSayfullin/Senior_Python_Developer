from qiskit import QuantumCircuit, execute, Aer

# Содаем квантовую цепь с 2 кубами
qc = QuantumCircuit(2, 2)

# Добавляем в цепь gate H (Адамара) на кубит 0
qc.h(0)

# добавляем gate CX (CNOT) между кубитами 0 и 1
qc.cx(0, 1)

# Измеряем кубиты
qc.measure([0, 1], [0, 1])

# выполняем симуляцию цепи на компьютере
backend = Aer.get_backend('gasm_simulator')
job = execute(qc, backend)
result = job.result()

# Выводим результат измерений
print(result.get_counts(qc))

# Здесь мы создали простую квантовую цепь, выполнили ее
# симуляцию с помощью Qiskit и вывели результаты измерений.
