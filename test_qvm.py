from pyquil import Program, get_qc
from pyquil.gates import H, CNOT, MEASURE

program = Program()
ro = program.declare("ro", "BIT", 2)

program += H(0)
program += CNOT(0, 1)

program += MEASURE(0, ro[0])
program += MEASURE(1, ro[1])

program.wrap_in_numshots_loop(10)

# Select the external QVM
qc = get_qc("2q-qvm")

# Compile using quilc
executable = qc.compile(program)

# Run using QVM
result = qc.run(executable)

print(result.get_register_map()["ro"])