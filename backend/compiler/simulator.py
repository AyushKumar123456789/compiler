def simulate(machine_code):
    registers = [0] * 8  # 8 general-purpose registers
    memory = {}

    for instruction in machine_code:
        opcode = instruction[:4]
        register = int(instruction[4:8], 2)
        value = int(instruction[8:], 2)

        if opcode == '0001':  # Load immediate (LI)
            registers[register] = value
        elif opcode == '0010':  # Store (STORE)
            memory[f'var_{register}'] = registers[register]

    return {
        'registers': registers,
        'memory': memory
    }
