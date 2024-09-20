instruction_set = {
    'LI': '0001',   # Load immediate
    'STORE': '0010',  # Store in memory
}

def assemble(assembly_code):
    binary_code = []
    
    for line in assembly_code.splitlines():
        parts = line.split()
        opcode = parts[0]
        register = parts[1].replace('R', '')  # Remove the 'R' from register
        value = parts[2]
        
        # Convert the instruction into binary (simplified for this demo)
        binary_code.append(instruction_set[opcode] + format(int(register), '04b') + format(int(value), '08b'))
    
    return binary_code
